n = int(input())
k = int(input())
 
x = tuple([int(t)for t in input().split()]) 
 
ans = 0
for x_i in x:
  if k-x_i>x_i:
    ans+=x_i*2
  else:
    ans+=(k-x_i)*2
    
print(ans)