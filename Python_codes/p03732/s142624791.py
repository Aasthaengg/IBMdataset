n,m=map(int,input().split())
w=[0]*n 
v=[0]*n
from collections import Counter
l=[]
for i in range(n):
    a,b=map(int,input().split())
    w[i]=a  
    v[i]=b 
a=min(w)
c=Counter(w)
#print(a)
cnt1=c[a]
#print(c)
v1=[v[i] for i in range(n) if w[i]==a]
v1.sort(reverse=1)
cnt2=c[a+1]
v2=[v[i] for i in range(n) if w[i]==a+1]
cnt3=c[a+2]
v3=[v[i] for i in range(n) if w[i]==a+2]
v2.sort(reverse=1)
v3.sort(reverse=1)
cnt4=c[a+3]
v4=[v[i] for i in range(n) if w[i]==a+3]
v4.sort(reverse=1)
#print(cnt1)
pv1=[0]*(cnt1+1)
pv1[0]=0
for i in range(1,cnt1+1):
    pv1[i]=pv1[i-1]+v1[i-1]
pv2=[0]*(cnt2+1)  
pv2[0]=0
for i in range(1,cnt2+1):
    pv2[i]=pv2[i-1]+v2[i-1]
pv3=[0]*(cnt3+1) 
pv3[0]=0
for i in range(1,cnt3+1):
    pv3[i]=pv3[i-1]+v3[i-1]
ans=0 
pv4=[0]*(cnt4+1)
for i in range(1,cnt4+1):
    pv4[i]=pv4[i-1]+v4[i-1]
for i in range(0,cnt1+1):
    for j in range(0,cnt2+1):
        for k in range(0,cnt3+1):
            for z in range(0,cnt4+1):
                if (i)*a+(j)*(a+1)+(k)*(a+2)+z*(a+3)<=m:
                    ans=max(ans,pv1[i]+pv2[j]+pv3[k]+pv4[z])
print(ans)