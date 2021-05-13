k=int(input())

def gcd(a,b):
  if b == 0:
    return a
  return gcd(b, a%b)

def gcd3(a,b,c):
  gcd_ab = gcd(a,b)
  return(gcd(gcd_ab,c))


sum_gcd = 0
for i in range(1,k+1):
  for j in range(1,k+1):
    for n in range(1,k+1):
      sum_gcd += gcd3(i,j,n)
print(sum_gcd)