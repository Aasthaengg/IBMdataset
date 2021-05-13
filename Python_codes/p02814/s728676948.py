from fractions import gcd

N, M = map(int, input().split())
As = list(map(int, input().split()))

a = As[0]
k = 0
while a % 2 == 0:
  a //= 2
  k += 1
lst = [As[0]//2]

for i in range(1,N):
  j = 0
  a = As[i]
  while a % 2 == 0:
    a //= 2
    j += 1
  if k != j:
    print(0)
    exit()
  lst.append(As[i]//2)
  
lcm = lst[0]
for i in range(1,N):
  t = gcd(lcm, lst[i])
  lcm *= lst[i]//t
  if lcm > M:
    print(0)
    exit()
  
rlt = M //lcm
if rlt % 2 == 0:
  print(rlt//2)
else:
  print(rlt//2+1)