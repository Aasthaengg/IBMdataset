N=int(input())
P=[int(input()) for i in range(N)]
pos=[-1]*N
for i,p in enumerate(P):
    pos[p-1]=i
x,mx=0,0
for i in range(N-1):
    if pos[i]<pos[i+1]:
        x+=1
        mx=max(mx,x)
    else:
        x=0
print(N-mx-1)