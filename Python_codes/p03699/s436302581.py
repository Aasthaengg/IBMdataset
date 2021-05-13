n=int(input())
l=[]
for _ in range(n):
  l.append(int(input()))
l.sort()
non_0s=[x%10!=0 for x in l]

if not any(non_0s):
  print(0)
  exit()

ans=sum(l)
if ans%10==0:
  for i in range(n):
    if non_0s[i]:
      ans-=l[i]
      break
print(ans)