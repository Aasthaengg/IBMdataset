from collections import Counter
n=int(input())
v=list(input().split())
v1=Counter(v[0::2]).most_common()
v2=Counter(v[1::2]).most_common()
ans=0
if v1[0][0]!=v2[0][0]:
  ans=(len(v[0::2])-v1[0][1])+(len(v[1::2])-v2[0][1])
elif len(v1)==1 and len(v2)==1:
  ans=min(v1[0][1],v2[0][1])
elif len(v1)==1:
  ans=len(v[1::2])-v2[1][1]
elif len(v2)==1:
  ans=(len(v[0::2])-v1[1][1])
else:
  ans=min((len(v[0::2])-v1[1][1])+(len(v[1::2])-v2[0][1]),(len(v[0::2])-v1[0][1])+(len(v[1::2])-v2[1][1]))
print(ans)