n,t = map(int, input().split())
a = []
for i in range(n):
    aa = list(map(int, input().split()))
    a.append(aa)

cost = float(10000)
for a in a:
    if a[1] <= t and a[0] < cost:
        cost = a[0]

if cost == 10000:
    cost = 'TLE'
print(cost)
