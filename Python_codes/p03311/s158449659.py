from collections import defaultdict
d = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
  a[i]-=i+1
  d[a[i]]+=1
ans=0
b = min(a)
for i in a:
  ans+=i-b
a = sorted(set(a))
c = 0
i = 0
while i<len(a)-1:
  c+=d[a[i]]
  if c-(n-c)>0:
    print(ans)
    exit()
  ans+=(c-(n-c))*(a[i+1]-a[i])
  i+=1
print(ans)