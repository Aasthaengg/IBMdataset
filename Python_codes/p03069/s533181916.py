N = int(input())
S = input()
max_w = S.count(".")
if max_w == 0 or max_w == N:
  print(0)
  exit()

ans = float("inf")
b, w = 0, max_w
for s in S:
  if s == "#":
    b += 1
  else:
    w -= 1
  ans = min(ans, b+w)
print(min(ans, max_w, N-max_w))
