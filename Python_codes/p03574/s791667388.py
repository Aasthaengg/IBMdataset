def solve():
  H, W = map(int, input().split())
  S = [0]*(H+2)
  S[0] = '*'*(W+2)
  S[H+1] = '*'*(W+2)
  for h in range(1,H+1):
    S[h] = '*' + input() + '*'
  ans = [[0]*W for _ in range(H)]
  dh = [1,1,1,0,-1,-1,-1,0]
  dw = [1,0,-1,-1,-1,0,1,1]
  for h in range(1,H+1):
    for w in range(1,W+1):
      if S[h][w]=='#':
        ans[h-1][w-1]='#'
        continue
      for i in range(8):
        if S[h+dh[i]][w+dw[i]]=='#':
          ans[h-1][w-1] += 1
    ans[h-1] = ''.join(map(str,ans[h-1]))
  return ans
print(*solve(),sep='\n')