def gcd(a,b):
  if a<b:
    a,b=b,a
  while a%b>0:
    a,b=b,a%b
  return b

def lcm(a,b):
  return (a//gcd(a,b))*b

N,M=map(int,input().split())
S=input()
T=input()

length=lcm(N,M)
S=S[::length//M]
T=T[::length//N]
if S==T:
  print(length)
else:
  print(-1)
