n=int(input())
r=0
a=[0]*n

def lambda_a(s):
  return 1/int(s)

a[:]=map(lambda_a,input().split())
for ii in range(n):
  r+=a[ii]
print(1/r)