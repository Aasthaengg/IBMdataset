n = int(input())
v = list(map(int, input().split()))
v.sort()
ans = v[0]
for i, x in enumerate(v[1:]):
    ans += ((2**i) * x)
print(ans/(2**(n-1)))