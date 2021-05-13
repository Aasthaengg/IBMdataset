import functools
MOD=10**9+7
def euclid(a, b):
  if b == 0:
    return a
  else:
    return euclid(b, a%b)

def multiple(a, b):
  return a*b // euclid(a, b)

def lcm(nums):
  return functools.reduce(multiple, nums)
n=int(input())
a=list(map(int,input().split()))
x=lcm(a)
sum=0
for i in range(n):
    sum+=x//a[i]
print(sum%MOD)