H, W = list(map(int, input().split()))
ans = []

for i in range(0,H):
  arr = input()
  ans.append(arr)
  ans.append(arr)

for i in range(0,H*2):
  print(ans[i])