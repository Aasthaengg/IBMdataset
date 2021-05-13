n=int(input())
c=[int(input())for i in range(n)]
l=[-1]*(max(c)+1)
d=[0]*(n+1)
d[0]=1
for i in range(1,n+1):
 d[i]=d[i-1];C=l[c[i-1]]
 if i-1!=C!=-1:d[i]+=d[C]
 l[c[i-1]]=i;d[i]%=(10**9+7)
print(d[n])