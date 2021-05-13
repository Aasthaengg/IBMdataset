x=int(input())
ans=1
while True:
  if x*ans%360==0:
    print(ans)
    break
  else:
    ans=ans+1