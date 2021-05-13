n,m,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ruia=[0]
ruib=[0]
mx=0
for (i,j) in zip(a,range(n)):
  ruia.append(ruia[j]+i)

for (i,j) in zip(b,range(m)):
  ruib.append(ruib[j]+i)
ans=0
for i in range(n+1):
  if ruia[i] > k:
    break
  while ruib[m] > k - ruia[i]:
    m -= 1
  ans = max(ans, i + m)
print(ans)

