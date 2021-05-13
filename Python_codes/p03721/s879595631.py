n,k=map(int,input().split())

x=[list(map(int,input().split())) for i in range(n)]
x.sort(key=lambda x:x[0])

for i in x:
  k-=i[1]
  if k<=0:
    print(i[0])
    exit()