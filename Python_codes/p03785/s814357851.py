import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    N, C, K = [int(x) for x in input().split()]
    T = [int(input()) for _ in range(N)]
    
    T.sort()

    ans = 1
    cnt = 1
    mi = T[0]
    for i in range(1, N):
        if cnt == C:
            ans += 1
            cnt = 1
            mi = T[i]
        else:
            if T[i] > mi + K:
                ans += 1
                cnt = 1
                mi = T[i]
            else:
                cnt += 1

    print(ans)

    
    
    

if __name__ == '__main__':
    main()

