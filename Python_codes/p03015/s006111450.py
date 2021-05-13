l=input()[::-1]
m=10**9+7
ans=1
p=1
for i in range(len(l)):
  if l[i]=='1':
    ans=(ans*2+p)%m
  p=(p*3)%m
print(ans)