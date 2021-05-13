from collections import defaultdict
d=defaultdict(int)
w=input()
s=len(w)
for i in range(s):
  d[w[i]]+=1
ans=0
for i in d:
  ans+=d[i]*(s-d[i])
  #print(d[i])
print(ans//2+1)