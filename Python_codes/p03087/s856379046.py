from itertools import permutations

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, Q = mi()
    S = input()
    lr = [map(int, input().split()) for _ in range(Q)]
    l, r = [list(i) for i in zip(*lr)]

    dp = [0]*(N+1)
    for i in range(N):
        if S[i-1:i+1] == 'AC':
            dp[i+1] = dp[i] + 1
        else:
            dp[i+1] = dp[i]

    for i in range(Q):
        ans = dp[r[i]]-dp[l[i]]
        print(ans)

if __name__ == '__main__':
    main()