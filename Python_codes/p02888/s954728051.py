import bisect
import collections
N=int(input())
L=list(map(int,input().split()))
L.sort()
c = collections.Counter(L)
#print(L)
 
#b-a < c < a+b

#a<=b<=c
ans=0
L_a=L[:N-2]
for i,a in enumerate(L_a):
    L_b=L[i+1:N-1]
    for j,b in enumerate(L_b,start=i+1):
        x=bisect.bisect(L[j+1:],a+b)
        ans+=x
        if a+b==L[j+x]:
            #print(a,b,L[j+x])
            ans-=c[a+b]
        #print(i,a,j,b,x,N-j-1,L[j+1:])
print(ans)