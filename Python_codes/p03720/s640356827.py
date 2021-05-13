n,m = map(int,input().split())
city = []
for i in range(n):
    city.append([])

for i in range(1,m+1):
    a,b = map(int,input().split())
    city[a-1].append(b)
    city[b-1].append(a)

for r in city:
    print (len(r))
