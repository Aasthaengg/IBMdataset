N = int(input())
H = list(map(int,input().split()))

res = 0
cnt = 0

for i in range(N-1):
  if H[i] >= H[i+1]:
    cnt += 1
    if i == N-2:
      res = max(res,cnt)
  else:
    res = max(res,cnt)
    cnt = 0
    
print(res)