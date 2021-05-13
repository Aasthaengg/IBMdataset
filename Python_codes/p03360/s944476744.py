a,b,c = map(int,input().split())
n = int(input())
m = max(a,b,c)
def bai(x):
  return 2*x

for i in range(n):
  m = bai(m)

print(m-max(a,b,c) +a+b+c)