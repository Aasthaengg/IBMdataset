abc=[int(x) for x in input().split()]
abc.sort()
a=abc[0]
b=abc[1]
c=abc[2]

ans=float('inf')
for i in range(a,100):
  for j in range(b,100):
    for k in range(c,100):
      now=0
      if i==j and j==k and i==k:
        now=i-a+j-b+k-c
        if now%2==0:
          ans=min(now//2,ans)
          break
        
print(ans)