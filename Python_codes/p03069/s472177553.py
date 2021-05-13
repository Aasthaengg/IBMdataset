n = int(input())
s=input()
if ('.' not in s) or ('#' not in s):
    print(0)
    exit()
bc = [0 for i in range(n)]
wc = [0 for i in range(n)]
for i in range(n):
  if s[i] == '#':
    bc[i] = 1
  else:
    wc[i] = 1
for i in range(n-1):
  bc[i+1] += bc[i]
for i in range(n-1,0,-1):
  wc[i-1] += wc[i]
ans = min(wc[0],bc[-1])
for i in range(n-1):
  ans = min(ans,bc[i]+wc[i+1])
print(ans)