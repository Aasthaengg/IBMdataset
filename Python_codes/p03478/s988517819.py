N,A,B=map(int,input().split())
res = 0

def check(a):
  sumsum = 0
  while a > 0:
    sumsum += a % 10
    a = a // 10
  return sumsum

for i in range(N+1):
  if A<=check(i)<=B:
    res += i
print(res)