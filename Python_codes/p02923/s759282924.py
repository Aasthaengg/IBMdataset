N = int(input())
hhh = list(map(int, input().split()))
m = 0
ans = 0
for i in range(N - 1):
    if hhh[i] >= hhh[i + 1]:
        m += 1
        ans = max(ans, m)
    else:
        m = 0
print(ans)
