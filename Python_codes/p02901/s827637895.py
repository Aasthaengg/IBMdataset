import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    price = [0]*m
    typesnum = [0]*m
    types = [[] for _ in range(m)]
    for i in range(m):
        price[i], typesnum[i] = map(int, input().split())
        types[i] = list(map(lambda x: int(x)-1, input().split()))
    dp = [10**9]*(1 << n)
    dp[0]=0
    for bit in range(1 << n):
        for i in range(m):
            keybit = 0
            for op in types[i]:
                keybit |= 1 << op
            dp[bit | keybit] = min(dp[bit | keybit], dp[bit]+price[i])
    if dp[-1] == 10**9:
        dp[-1] = -1
    print(dp[-1])


if __name__ == '__main__':
    main()