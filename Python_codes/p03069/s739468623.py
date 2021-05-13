N,S = open(0).read().split()
ans = 0
ls = []
cnt = 1
p = S[0]
for c in S[1:]:
  if p!=c:
    p = c
    ls.append(cnt)
    cnt = 1
  else:
    cnt += 1
ls.append(cnt)
b = 0
w = 0
if S[0]=='.':
  w = sum(ls[i] for i in range(0, len(ls),2))
  ans = b+w
  for i in range(len(ls)):
    if i%2==0:
      w -= ls[i]
    else:
      b += ls[i]
    ans = min(ans,w+b)
else:
  w = sum(ls[i] for i in range(1,len(ls),2))
  ans = b+w
  for i in range(len(ls)):
    if i%2==0:
      b += ls[i]
    else:
      w -= ls[i]
    ans = min(ans,w+b)

print(ans)