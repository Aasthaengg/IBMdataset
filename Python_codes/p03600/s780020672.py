import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())
    A = [[int(i) for i in readline().split()] for _ in range(N)]

    via_min = [[10**15] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if k == i or k == j:
                    continue
                via_min[i][j] = min(via_min[i][j], A[i][k] + A[k][j]) 

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if via_min[i][j] < A[i][j]:
                print(-1)
                exit()
            elif via_min[i][j] == A[i][j]:
                continue
            else:
                ans += A[i][j]
    
    print(ans)


if __name__ == "__main__":
    main()
