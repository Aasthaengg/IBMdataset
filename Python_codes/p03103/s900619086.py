n,k=map(int,input().split())
s=0
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l.sort()
for i in range(n):
    if(l[i][1]<=k):
        s+=l[i][0]*l[i][1]
        k-=l[i][1]
    else:
        s+=l[i][0]*k
        k=0
    if(k==0):
        break
print(s)
