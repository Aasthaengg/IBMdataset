n = int(input())
a = list(map(int, input().split()))

snuke = 0
bear = sum(a)
ans = float('inf')

for i in range(n-1):
    snuke += a[i]
    bear -= a[i]
    if abs(snuke - bear) < ans:
        ans = abs(snuke - bear)

print(ans)