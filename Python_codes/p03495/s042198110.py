from collections import Counter
n,k=map(int,input().split())

a=[int(i) for i in input().split()]
d=Counter(a)
a=sorted(list(d.items()),key=lambda x:x[1],reverse=True)
if len(a)<=k:
    print(0)
else:
    ans=0
    for i in range(k,len(a)):
        ans+=a[i][1]
    print(ans)
    

