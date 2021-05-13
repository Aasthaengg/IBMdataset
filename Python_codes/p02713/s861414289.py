K = int(input())

def gcd(a,b):
  if(a<b):
    temp = a
    a = b
    b = temp
  if(a%b==0):
    return b;
  else:
    return gcd(a%b,b);

sum = 0

for a in range(1,K+1):
  for b in range(1,K+1):
    for c in range(1,K+1):
      temp=gcd(a,b)
      sum+=gcd(c,temp)

print(sum)
