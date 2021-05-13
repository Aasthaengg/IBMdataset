N = int(input())
b = list(map(int, input().split()))
ans = []
cnt = 0
while len(b): 
  for j in range(len(b)-1, -1, -1):
    if b[j] == j+1:
      ans += [b.pop(j)]
      break
  cnt += 1
  if cnt >= N+1:
    print(-1)
    exit()
    
for n in ans[::-1]:
  print(n)