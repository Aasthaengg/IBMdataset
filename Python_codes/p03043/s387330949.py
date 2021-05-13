n,k = map(int,input().split())

def f(x,y):
  cnt = 0
  while x > y:
    y = y << 1
    cnt +=1
  return cnt

ans = 0
for i in range(1,n+1):
  i2 = bin(i)
  cnt = f(k,i)
  ans += 0.5**cnt

print(ans/n)