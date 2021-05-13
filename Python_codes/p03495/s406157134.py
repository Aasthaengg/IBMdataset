from collections import Counter
n,k=map(int,input().split())
a=list(input().split())
c=Counter(a).most_common()
cnt=len(set(a))-k
ans=0
for i in range(cnt):
  ans+=c[i*(-1)-1][1]
print(ans)