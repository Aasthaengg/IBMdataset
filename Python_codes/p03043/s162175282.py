N, K = map(int, input().split())

ans = 0

def calc(x, goal):
    res = 0
    while x < goal:
        x *= 2
        res += 1
    return res    


for i in range(1, N+1):
    cnt = calc(i, K)
    ans += 1 / N * ((1 / 2) ** cnt)

print(ans)