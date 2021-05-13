N = int(input())
H = list(map(int, input().split()))
ans = 0
while sum(H):
  f = 0
  for i in range(N):
    if f == 0:
      if H[i] > 0:
        f = 1
        H[i] -= 1
        ans += 1
    else:
      if H[i] > 0:
        H[i] -= 1
      else:
        f = 0
print(ans)