a=list(input())
c=[chr(i) for i in range(97, 97+26)]
ct=[0 for i in range(26)]
n=len(a)
for i in range(n):
  ct[c.index(a[i])]+=1
ans=0
for i in range(26):
  ans+=(n-ct[i])*ct[i]
print(ans//2+1)