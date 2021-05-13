n,m = map(int,input().split())
a = []
for i in range(m):
    a.extend(list(map(int,input().split())))
for i in range(1,n+1):
    print(a.count(i))