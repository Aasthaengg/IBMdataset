N = int(input())
ans = 0

for n in range(N+1):
  if n%2==1:
    Y = 0
    for m in range(1,N+1):
      if n%m==0:
        Y+=1
    if Y==8:
      ans+=1
    
print(ans)