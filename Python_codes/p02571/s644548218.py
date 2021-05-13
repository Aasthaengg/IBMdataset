s=input()
t=input()

ans=10*100

for i in range(len(s)):
  ss=len(t)+i
  a=s[i:ss]
  if len(t) != len(a):
    continue
  aaa=0
  for j in range(len(t)):
    if t[j] != a[j]:
      aaa+=1
  ans=min(ans,aaa)
print(ans)