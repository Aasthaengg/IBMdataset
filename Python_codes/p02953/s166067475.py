N = int(input())
H = list(map(int, input().split()))
H.reverse()
f = 0
h = H[0]
for i in range(1, N):
  if H[i] >= h + 2:
    print("No")
    f = 1
    break
  else:
    h = min(h, H[i])
if f == 0:
  print("Yes")