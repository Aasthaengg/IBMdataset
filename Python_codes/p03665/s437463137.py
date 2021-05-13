from math import factorial 
def comb(n, r):
  return factorial(n)//(factorial(n-r)*factorial(r))

n,p = map(int,input().split())
al = list(map(int,input().split()))
even = 0
odd = 0
for a in al:
  if a%2 == 0:
    even += 1
  else:
    odd += 1
if p == 1 and odd == 0:
  print(0)
  exit()
ans1 = 2**even
ans2 = 0
if p == 0:
  t = 0
  while t <= odd:
    ans2 += comb(odd,t)
    t += 2
else:
  k = 1
  while k <= odd:
    ans2 += comb(odd,k)
    k += 2
print(ans1*ans2)