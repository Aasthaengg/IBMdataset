n = int(input())
p = list(map(int, input().split()))

m = n + 1
ans = 0
for i in p:
    if i <= m:
        ans += 1
    m = min(m, i)
print(ans)
