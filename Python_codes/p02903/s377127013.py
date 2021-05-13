H,W,A,B = map(int,input().split())
ans = [[0]*W for i in range(H)]
for i in range(A):
  for j in range(B):
    ans[j][i] = 1

for i in range(A,W):
  for j in range(B,H):
    ans[j][i] = 1

for l in ans:
  for i in l:
    print(i,end="")
  print()