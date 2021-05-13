from collections import Counter
n,a,b=map(int,input().split())
V=list(map(int,input().split()))
V.sort()
N=50
bikkuri=[1 for i in range(N+1)]
for i in range(N):
    bikkuri[i+1]=(i+1)*bikkuri[i]
def comb(a,b):
    if b==0:
        return 1
    else:
        return bikkuri[a]//(bikkuri[a-b]*bikkuri[b])
ans1=0
ans2=0
if V[-a]==V[-1]:
    ans1=V[-1]
    VC=Counter(V)
    num=VC[ans1]
    for i in range(a,min(b,num)+1):
        ans2+=comb(num,i)
else:
    ans1=sum(V[-a:])/a
    A=list(set(V[-a:]))
    VC=Counter(V)
    num1=VC[V[-a]]
    VaC=Counter(V[-a:])
    num2=VaC[V[-a]]
    ans2=comb(num1,num2)
print(ans1)
print(ans2)