N = int(input())
Ali = list(map(int,input().split()))
res = 10**10

for i in range(N):
  r = 0
  while Ali[i]%2 == 0:
    Ali[i] //= 2
    r += 1
  res = min(res,r)
  
print(res)