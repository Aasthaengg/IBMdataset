import sys

readline = sys.stdin.readline
N = int(input())
shop = [int(readline().replace(' ', ''), 2) for _ in range(N)]
profits = [list(map(int, readline().split())) for _ in range(N)]
ans = -10**20
for bit in range(1, 1<<10+1):
    profit = 0
    cnt = 0
    for s, p in zip(shop, profits):
        num = bin(bit&s).count('1')
        if num:
            cnt += 1
        profit += p[num]
    if cnt and ans < profit:
        ans = profit
print(ans)
