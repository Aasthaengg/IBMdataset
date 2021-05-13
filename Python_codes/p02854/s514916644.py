import bisect


n = int(input())
la = [int(w) for w in input().split()]
la_sum = [0]*(n)
ans = 10**10

la_sum[0] = la[0]
for i in range(1, n):
    la_sum[i] = la_sum[i-1] + la[i]


for i in range(0, n):
    l = la_sum[i]
    r = la_sum[-1]-la_sum[i]
    d = abs(l-r)
    ans = min(ans, d)
print(ans)
