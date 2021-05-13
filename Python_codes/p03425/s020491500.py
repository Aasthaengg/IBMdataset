ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()

m=0
a=0
r=0
c=0
h=0

for i in range(n):
  k=input()[0]
  if k=='M':
    m+=1
  if k=='A':
    a+=1
  if k=='R':
    r+=1
  if k=='C':
    c+=1
  if k=='H':
    h+=1

cnts = [m,a,r,c,h]

ans=0
for i in range(5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      cs = [cnts[i],cnts[j],cnts[k]]
      ans += cs[0]*cs[1]*cs[2]
print(ans)

