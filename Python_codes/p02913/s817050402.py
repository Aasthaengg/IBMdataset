n=int(input())
s=input()
import collections
l=0
h=n//2+1
ans=0
while h>l+1:
    t=(h+l)//2
    d=collections.defaultdict(int)
    for i in range(n-t+1):
        c=s[i:i+t]
        if d[c]==0:
            d[c]=i+1
        else:
            if d[c]+t<=i+1:
                l=t
                break
    else:
        h=t
print(l)