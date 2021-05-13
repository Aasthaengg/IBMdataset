n,k = map(int,input().split())
p = list(map(int,input().split()))

for i in range(n):
    p[i] += 1

ans = []

a = [0] * (n + 1)
for i in range(n):
    a[i+1] = p[i] + a[i]

t = 0
for i in range(k,n+1):
    t = max(t, a[i] - a[i-k])

print(t/2)
