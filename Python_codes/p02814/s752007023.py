def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)

def lcm(a,b):
  return a*b//(gcd(a,b))

N,M=map(int,input().split())
A=list(map(int,input().split()))

LCM=1
for i in A:
  i=i//2
  LCM=lcm(i,LCM)

for i in A:
  i=i//2
  if (LCM//i)%2==0:
    print(0)
    exit()

ans=((M//LCM)+1)//2
print(ans)