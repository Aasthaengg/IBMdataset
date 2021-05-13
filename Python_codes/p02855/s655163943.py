H, W, K = map(int, input().split())
S = []
for i in range(H):
  s = str(input())
  S.append(s)
  
ans = [[0]*W for i in range(H)]

cnt = 1
for i in range(H):
  s = S[i]
  if '#' in s:
    flag = False
    for j in range(W):
      if s[j] == '#':
        if flag:
          cnt += 1
        else:
          flag = True
      ans[i][j] = cnt
    cnt += 1
    
def blank(l):
  global H
  global W
  for i in range(H):
    if l[i] == [0]*W:
      if (i<H-1) and (l[i+1]!=[0]*W):
        l[i] = l[i+1]
      elif (i>0) and (l[i-1]!=[0]*W):
        l[i] = l[i-1]
  return l
        
while [0]*W in ans:
  ans = blank(ans)
for i in range(H):
  l = ans[i]
  print(*l)