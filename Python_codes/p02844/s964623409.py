n = int(input())
s = list(input())
a = ['0','1','2','3','4','5','6','7','8','9']
g = []
for i in a:
  for j in a:
    for k in a:
      g.append([i,j,k])
cnt=0
for i in g:
  d =0
  e =0
  while d < n:
    if s[d] == i[e]:
      e+=1
    d+=1
    if e==3:
      cnt+=1
      break
print(cnt)