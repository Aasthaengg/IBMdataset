n=int(input())
for i in range(1,361):
  if n*i%360==0:
    ans=i
    break
print(ans)