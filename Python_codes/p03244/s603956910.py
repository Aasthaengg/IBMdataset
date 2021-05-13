from collections import Counter
n=int(input())
v=list(input().split())
v1=Counter(v[0::2]).most_common()
v2=Counter(v[1::2]).most_common()
ans=0
v1.append([0,0])
v2.append([0,0])
if v1[0][0]!=v2[0][0]:
  ans=n-v1[0][1]-v2[0][1]
else:
  ans=min(n-v1[1][1]-v2[0][1],n-v1[0][1]-v2[1][1])
print(ans)