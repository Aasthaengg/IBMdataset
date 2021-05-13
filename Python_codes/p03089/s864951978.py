from sys import exit

n = int(input())
b = list(map(int, input().split()))

cnt = [0] * n
done = [False] * n
ans = [0] * n
for i in range(n):
  for j in range(n-1, -1, -1):
    if done[j]:
      continue
    if b[j] == cnt[j] + 1:
      ans[i] = b[j]
      for k in range(j+1, n):
        cnt[k] += 1
      done[j] = True
      break
        
for i in range(n):
  if not done[i]:
    print(-1)
    exit()
    
for i in range(n):
  print(ans[i])