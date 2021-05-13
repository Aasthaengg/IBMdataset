#%%
n, m = map(int, input().split())
a = list(map(int, input().split())) 

a[0] %= m
for i in range(1, n):
    a[i] += a[i-1]
    a[i] %= m
a.append(0)

count = {}
for i in range(n+1):
    count[a[i]] = 0
for i in range(n+1):
    count[a[i]] += 1

c = list(count.values())
ans = 0
for i in range(len(c)):
    tmp = c[i] * (c[i]-1) // 2
    ans += tmp
print(ans)