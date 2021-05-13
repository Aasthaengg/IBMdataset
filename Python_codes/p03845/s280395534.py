n=int(input())
t=[0]+[int(x) for x in input().split()]
m=int(input())
for _ in range(m):
    x,y=map(int,input().split())
    tt=t[:]
    tt[x]=y
    print(sum(tt))
    
