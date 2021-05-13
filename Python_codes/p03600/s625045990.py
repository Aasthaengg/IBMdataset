import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())
    A = [[int(i) for i in readline().split()] for _ in range(N)]

    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            d = A[i][j]
            flag = True
            for k in range(N):
                if k == i or k == j:
                    continue
                
                tmp = A[i][k] + A[k][j]
                if tmp < d:
                    print(-1)
                    exit()
                
                elif tmp == d:
                    flag = False
                    break
            if flag:
                ans += d
    
    print(ans)


if __name__ == "__main__":
    main()
