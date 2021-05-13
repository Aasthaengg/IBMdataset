S=input()

dp=[False]* (len(S)+1)

dp[0] = True

for i in range(1, len(dp)):
  for w in [ 'dream', 'dreamer', 'erase', 'eraser']:
    if dp[i-len(w)] and w == S[i-len(w):i]:
      dp[i] = True

if dp[-1]:
  print('YES')
else:
  print('NO')

    
