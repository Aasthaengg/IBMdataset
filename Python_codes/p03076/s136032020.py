K=[int(input()) for _ in range(5)]
ans=0
c=10
for i in range(5):
  r=K[i]%10
  if r==0:
    r=10
  c=min(r,c)
for k in range(5):
  if K[k]%10==0:
    ans+=K[k]
  else:
    ans+=(K[k]//10)*10+10
print(ans-10+c)