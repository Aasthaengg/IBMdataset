N = int(input())
B = list(map(int, input().split()))

ans = []
for i in range(N):
  flag = True
  for j in range(N-i):
    n = N-i-j
    if B[n-1] == n:
      ans.append(n)
      B.pop(n-1)
      flag = False
      break
  if flag:
    break
    
if flag:
  print(-1)
else:
  ans.reverse()
  for i in range(N):
    print(ans[i])