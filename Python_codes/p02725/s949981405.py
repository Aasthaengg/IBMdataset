k, n = map(int,input().split())
a = list(map(int,input().split()))

a = sorted(a)

d = []
d.append(k-a[n-1]+a[0])

for i in range(n-1):
    d.append(a[i+1]-a[i])

print(k-max(d))
