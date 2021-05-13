n,a,b,c,d = map(int,input().split())
s = input()
S = s[:max(c,d)]
#print(S)
l = len(S)
C = True
D = False
for i in range(l-1):
  if i >= min(a,b) and S[i]=='#' and S[i+1]=='#':
    C = False
    break
  if c > d and d > i >= max(a,b)-1:
    if S[i-1]=='.' and S[i]=='.' and S[i+1]=='.':
      D = True
      
if not C:
  print('No')
elif C and not D:
  if c < d:
    print('Yes')
  else:
    print('No')
else:
  print('Yes')