N = int(input())

ans = None
for h in range(1, 3501):
  for n in range(1, 3501):
    if 4*h*n - n*N - h*N != 0:
      w = (N * h * n) / (4*h*n - n*N - h*N)
      if w > 0 and w.is_integer() and 4/N == 1/h + 1/n + 1/w:
        ans = [h, n, int(w)]
        break
  if ans:
    break
print(" ".join(map(str, ans)))