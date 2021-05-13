N = int(input())
a = list(map(int, input().split()))

ans = 0
for i, ai in enumerate(a):
    if i + 1 == a[ai - 1]: ans += 1

ans //= 2
print(ans)