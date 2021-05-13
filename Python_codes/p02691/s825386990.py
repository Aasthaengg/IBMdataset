n=int(input())
a=[0]*n
a=list(map(int,input().split()))
L={}
R={}
ans=0
for i in range(n):
    L.setdefault(i-a[i],0)
    R.setdefault(i+a[i],0)
    L[i-a[i]]+=1
    R[i+a[i]]+=1
    
    if (i-a[i] in R):
        ans+=R[i-a[i]]
        #print(ans,L[i-a[i]])
    if (i+a[i] in L):
        ans+=L[i+a[i]]

print(ans)
#print(L)
#print(R)