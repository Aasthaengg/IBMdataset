def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)
N=int(input())
L=list(map(int,input().split()))
s=L[0]
for i in range(N-1):
  s=gcd(L[i+1],s)
print(s)