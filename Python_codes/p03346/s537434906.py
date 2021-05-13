import sys

input = sys.stdin.readline

def main():
    N = int(input())
    P = []
    for i in range(N):
        P.append((int(input()), i))
    P.sort(key=lambda x: x[0])
    Q = list(zip(*P))[1]
    cnt = 1; ans = 1
    for i in range(N-1):
        if Q[i] < Q[i+1]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)
    print(N-ans)

if __name__ == "__main__":
    main()
