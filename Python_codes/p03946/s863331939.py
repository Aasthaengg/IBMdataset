N,T = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
ans = []
mi = 10**9
for i in range(N):
    mi = min(mi,a[i])
    ans.append(a[i]-mi)
print(ans.count(max(ans)))