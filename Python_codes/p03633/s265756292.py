def gcd(a,b):
  if b == 0:return a
  return gcd(b,a%b)

N=int(input())
T=[]
if N==1:
  print(input())
  exit()
for i in range(N):
  t = int(input())
  T.append(t)
  if i == 0:continue
  elif i == 1:
    lcm = T[-2]*T[-1]//gcd(T[-2],T[-1])
  else:
    lcm = lcm * T[-1]//gcd(lcm,T[-1])

print(lcm)