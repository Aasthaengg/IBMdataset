from fractions import gcd
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = []
lcm = 1
for i in a:
    b.append(i//2)
for i in b:
  lcm = lcm // gcd(lcm,i) * i
ans = m // lcm
sum = 0
for i in b:
  if (lcm // i) % 2 == 1:
    sum += 1
if sum != len(a):
  print(0)
elif ans%2 ==1:
    print((ans+1)//2)
else:
    print(ans//2)