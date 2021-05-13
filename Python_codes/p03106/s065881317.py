A,B,K=map(int,input().split())
check = 0
res = 0
for i in range(100,0,-1):
  if A % i == 0 and B % i == 0:
    check += 1
    if check == K:
      res = i
      break
print(res)