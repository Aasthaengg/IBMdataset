from collections import Counter

n=int(input())
l=[int(i) for i in input().split()]
n=len(l)
l1=l[0::2]
l2=l[1::2]
c1=Counter(l1).most_common(2)
c2=Counter(l2).most_common(2)

if c1[0][0]!=c2[0][0]:
    ans=n-c1[0][1]-c2[0][1]
    print(int(ans))
else:
    if len(c1)==1 or len(c2)==1:
        print(n//2)
    else:
        res1=n-c1[1][1]-c2[0][1]
        res2=n-c1[0][1]-c2[1][1]
        ans=min(res1,res2)
        print(int(ans))
