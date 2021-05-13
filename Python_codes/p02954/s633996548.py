S = str(input())
s = []

tmp = 0
for i in range(len(S)-1):
  if S[i]=='L' and S[i+1]=='R':
    s.append(S[tmp:i+1])
    tmp = i+1
  elif i == len(S)-2:
    s.append(S[tmp:])
    
ans = [0]*len(S)
tmp = 0
for t in s:
  cnt = t.count('R')
  if len(t) % 2 == 0:
    ans[cnt+tmp-1], ans[cnt+tmp] = len(t)//2, len(t)//2
  else:
    if cnt % 2 == 0:
      ans[cnt+tmp-1], ans[cnt+tmp] = len(t)//2, len(t)//2+1
    else:
      ans[cnt+tmp-1], ans[cnt+tmp] = len(t)//2+1, len(t)//2
  tmp += len(t)
      
print(' '.join(map(str, ans)))