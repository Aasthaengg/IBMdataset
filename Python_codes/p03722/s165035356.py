n, m = map(int, input().split())
e = [tuple(map(int, input().split())) for _ in range(m)]
d = [-float('inf')]*(n+1)
d[1] = 0
for _ in range(n):
    for i,j,c in e:
        d[j] = max(d[j], d[i]+c)
t = d[n]
for _ in range(n):
    for i,j,c in e:
        d[j] = max(d[j], d[i]+c)

if t < d[n]:
    print('inf')
else:
    print(d[n])