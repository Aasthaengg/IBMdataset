n,k=map(int,input().split())
xy=[list(map(int,input().split())) for _ in [0]*n]
xy=sorted(xy,key=lambda x:x[0])
temp=[]
for i in range(n):
    for j in range(i+k-1,n):
        temp.append([xy[j][0]-xy[i][0]]+sorted([y for x,y in xy[i:j+1]]))
m=10**19      
for t in temp:
    l=len(t)-1
    for i in range(1,l-k+2):
        m=min(m,t[0]*(t[i+k-1]-t[i]))
print(m)