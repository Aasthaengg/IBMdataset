def divisors(n):
  ret=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      ret.append(i)
      if n//i!=i:
        ret.append(n//i)
  return ret

n = int(input())
ans = len(divisors(n-1)) - 1 

for d in divisors(n)[1:]:
  tmp = n
  while tmp%d == 0:
    tmp = tmp//d
  if tmp%d == 1:
    ans += 1
  
print(ans)