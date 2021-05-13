N = int(input())
data = []
cities = []

for i in range(1,N+1):
    c,p = input().split()
    data.append([c,-(int(p)),i])
    if c in cities:
        None
    else:
        cities.append(c)

cities.sort()

ans = []
for c in cities:
    b = [s for s in data if c in s]
    b.sort(key=lambda x: x[1])
    for i in range(len(b)):
        ans.append(b[i])

for i in range(N):
    print(ans[i][2])