from collections import Counter

n=int(input())
l=[int(i) for i in input().split()]
c=Counter(l).most_common()
s=sorted([key,val] for key,val in c if val>=2)

if len(s)<2:
    ans=0
elif s[-1][1]>=4:
    ans=s[-1][0]**2
else:
    ans=s[-1][0]*s[-2][0]

print(ans)
