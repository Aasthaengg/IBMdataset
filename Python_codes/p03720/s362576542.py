n,m = map(int,input().split())
city = [[0] for _ in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    city[a-1].append(b)
    city[b-1].append(a)
for i in city:
    print(len(i)-1)