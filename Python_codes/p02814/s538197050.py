from math import ceil
def gcd(a,b):
  while b:
    a,b = b,a%b  
  return a

def lcm(a,b):
  return a*b//gcd(a,b)  
  
n,m = map(int,input().split())
A = list(map(int,input().split()))

A = [a//2 for a in A]

pre = None
for a in A:
  c = 0
  while a % 2 ==0:
    a //= 2 
    c += 1    
  if pre is None:    
    pre = c
  elif pre != c:
    print(0)
    exit()

if n == 1:
  ans = A[0]
else:
  ans = lcm(A[0],A[1])  
  for i in range(n-2):  
    if ans > m:
      print(0)
      exit()
    ans = lcm(ans,A[i+2])  

print(ceil((m//ans)/2))  