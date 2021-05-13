from collections import Counter
n,k=map(int,input().split())
a=list(map(int,input().split()))
x=len(set(a))
#print(x)
C=Counter(a)
ans=0
#print(C)
C2 = sorted(C.items(), key=lambda x:x[1])
#print(C2)
if k>x:
    print(0)
else:
    for i in range(x-k):
        ans+=C2[i][1]
    print(ans)