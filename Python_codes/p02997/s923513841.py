# 中心に1をおき、(1,2),(1,3),(1,4)...を結んだグラフを作ると
# ペアの数は(N-1)C2できてこれが最大（これを超えるKの場合-1）
# ここから条件に合わせるためには、1を含まない要素のペアを直接結んでいけばよい。
# 全部結んだ場合でNC2になり、O(N^2)で10000 (実際5000弱)

N,K = map(int,input().split())

maxval = ((N-1)*(N-2)) // 2
if maxval < K:
  print(-1)
  exit(0)
  
ans = []

# まず1と各頂点を結んだグラフを構成する
for i in range(2,N+1):
  ans.append((1,i))
  
# そこから減らすべき頂点数
goal = maxval - K
i = 2
j = 3
while goal > 0:
  ans.append((i,j))
  if j + 1 > N:
    i += 1
    j = i + 1
  else:
    j += 1
  goal -= 1
  
print(len(ans))
for a in ans:
  print(*a)