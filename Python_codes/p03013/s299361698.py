n,m = map(int,input().split())
def Fib(n):
  seq = []
  a,b = 0,1
  for i in range(1,n+10):
    if i == 1:
      seq.append(0)
    elif i == 2:
      seq.append(1)
    else:
      a, b = b, a + b
      seq.append(b)
  return seq
table = Fib(n)
temp = -1
route = 1
mod = 10**9+7
for _ in range(m):
  a = int(input())
  dif = a-temp-1
  temp = a
  route = route*table[dif]%mod
print(route*table[n-temp]%mod)  