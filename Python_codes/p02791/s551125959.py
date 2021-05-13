n = int(input())
p = list(map(int,input().split()))
ans = 0
mn = float('inf')
for i in range(n):
    if p[i] < mn:
        ans += 1
    mn = min(mn,p[i])
print(ans)
