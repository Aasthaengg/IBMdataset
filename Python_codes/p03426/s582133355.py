H, W, D = map(int, input().split())
dic = {}
memo = [0]*(H*W+1)

for i in range(H):
  s = input().split()
  for j in range(W):
    dic[int(s[j])] = (i,j)
    
for i in range(1,H*W+1):
  if i - D >= 1:
    memo[i] = memo[i-D] + abs(dic[i][0]-dic[i-D][0]) + abs(dic[i][1]-dic[i-D][1])
    
Q = int(input())
for _ in range(Q):
  l, r = map(int, input().split())
  print(memo[r]-memo[l])