N = int(input())
Hs = list(map(int, input().split()))

cnt = 0
l = 0
r = 1
while max(Hs) > 0:
  if Hs[l] == 0:
    l += 1
    r = l + 1
  elif r < N and Hs[r] > 0:
    r += 1
  else:
    for i in range(l,r):
      Hs[i] -= 1
    cnt += 1
    r = l + 1
  
print(cnt)