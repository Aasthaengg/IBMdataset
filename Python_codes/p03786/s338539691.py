n = int(input())
a = list(map(int,input().split()))
a = sorted(a)
ans = 1
s = 0
q = 0
for i in range(n-1):
    s += a[i]
    if 2*s >= a[i+1]:
        q += 1
    else:
        q = 0
    if i == n-2:
        ans += q
print(ans)