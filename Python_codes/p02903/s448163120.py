H, W, A, B = map(int, input().split())
ans = [0]*H
for i in range(H):
  if i < B:
    ans[i] = "0"*A + "1"*(W-A)
  else:
    ans[i] = "1"*A + "0"*(W-A)
print(*ans, sep="\n")