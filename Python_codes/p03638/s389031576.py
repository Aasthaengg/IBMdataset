H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))
ans = [[0 for _ in range(W)] for _ in range(H)]
S = []
for i,a in enumerate(A):
  S+=[i+1]*a

for i in range(H):
  if i%2==0:
    for j in range(W):
      ans[i][j]=S.pop()
      
  else:
    for j in range(W-1,-1,-1):
      ans[i][j]=S.pop()
      
for a in ans:
  print(' '.join(map(str,a)))