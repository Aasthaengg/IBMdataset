N = int(input())
h = list(map(int, input().split()))
cnt = 0 
while True:
  pre = False
  for i in range(N):
    if h[i] > 0:
      if pre:
        h[i] -= 1
      else:
        h[i] -= 1
        pre = True
        cnt += 1
    else:
      pre = False
  if sum(h) == 0:
    break
print(cnt)
