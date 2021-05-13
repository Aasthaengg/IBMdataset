k,n = map(int,input().split())
a = list(map(int,input().split()))
t = 10 ** 6

for i in range(n - 1):
    a.append(a[i] + k)

for i in range(len(a)-n+1):
    t = min(t,a[i+n-1] - a[i])

print(t)