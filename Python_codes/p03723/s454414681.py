a,b,c=map(int,input().split())

if a%2!=0 or b%2!=0 or c%2!=0:
  print(0)
  exit()
elif a==b==c:
  print(-1)
  exit()
    
ans=0  

while a%2==0 and b%2==0 and c%2==0:
  num_a,num_b,num_c=a/2,b/2,c/2
  a=num_b+num_c
  b=num_a+num_c
  c=num_a+num_b
  ans+=1
print(ans)
