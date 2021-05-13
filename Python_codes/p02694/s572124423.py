X = int(input())
B = 100
ans = 0

while B<X:
  B+=B//100
  ans+=1
  
print(ans)