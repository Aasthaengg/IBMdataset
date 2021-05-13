import fractions
N = int(input())
t = []
for i in range(N):
  t.append(int(input()))
  
lcm = 1

for i in range(N):
  lcm = lcm* t[i]// fractions.gcd(lcm, t[i])
  
print(lcm)