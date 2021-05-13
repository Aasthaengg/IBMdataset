M=10**9+7
s=input()
r=range
k=[1]+[0]*12
for c in s:
  l=[0]*13
  for i in r(13):
    if c=='?':
      for j in r(10): l[(i*10+j)%13]+=k[i]
    else: l[(i*10+int(c))%13]+=k[i]
  for i in r(13): k[i]=l[i]%M
print(k[5])