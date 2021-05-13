n,m = map(int,input().split())
tmp=[]
for _ in range(m):
    tmp.append(list(map(int,input().split())))
for i in range(1,n+1):
    print(sum(j.count(i) for j in tmp))