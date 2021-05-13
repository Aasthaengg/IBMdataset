N,M=map(int,input().split())
S=input()
T=input()

def gcd(a,b):
  if a<b:
    a,b=b,a
  while a%b>0:
    a,b=b,a%b
  return b

def lcm(a,b):
  return (a//gcd(a,b))*b

length=lcm(N,M)
gapt=length//N
gaps=length//M
i=0
j=0
while i<N:
  if S[i]!=T[j]:
    print(-1)
    break
  else:
    i+=gaps
    j+=gapt
else:
  print(length)