import fractions
from functools import reduce
n,m=map(int,input().split())
a=list(map(int,input().split()))
last_cnt = 0
v=a[0]
while v%2==0:
  v//=2
  last_cnt+=1
for v in a[1:]:
  cnt = 0
  while v%2 == 0:
    v //=2
    cnt += 1
  if last_cnt != cnt:
    print(0)
    exit()
    
a=[v//2 for v in a]

def lcm_base(x,y):
  return (x*y)//fractions.gcd(x,y)
def lcm_list(numbers):
  return reduce(lcm_base, numbers, 1)

l = lcm_list(a)
if l>m:
  print(0)
  exit()
print(1+(m-l)//(l*2))
#print(lcm_list(a))