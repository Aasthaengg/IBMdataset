n=int(input())
f=0
for i in range(n):
  f=f*10+7
  f%=n
  if f==0:
    print(i+1)
    break
else:print(-1)