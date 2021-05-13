a=int(input())
b=int(input())
c=int(input())
x=int(input())

ans=0
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      num_500=500*i
      num_100=100*j
      num_50=50*k
      if num_500+num_100+num_50==x:
        ans+=1
        
print(ans)
