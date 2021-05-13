N=int(input())
u=[]
v=[]
for i in range(N):
    x,y=map(int,input().split())
    u.append(x+y)
    v.append(x-y)
print(max(max(u)-min(u),max(v)-min(v)))