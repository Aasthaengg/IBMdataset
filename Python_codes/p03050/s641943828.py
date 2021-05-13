def divisore(n):
  divisors=[]
  for i in range(1, int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)
  return divisors

n=int(input())
l=divisore(n)

ans=0
for i in l:
  i-=1
  if i!=0 and n//i==n%i:
    ans+=i
print(ans)