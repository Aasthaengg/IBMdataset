H, W, A, B = map(int, input().split())
for i in range(H):
  if i <= B-1:
    s = '1'*A + '0'*(W-A)
  else:
    s = '0'*A + '1'*(W-A)
  print(s)