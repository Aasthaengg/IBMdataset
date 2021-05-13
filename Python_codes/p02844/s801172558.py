import itertools
n = int(input())
s = list(input())
a = ['0','1','2','3','4','5','6','7','8','9']
cnt=0
for i in list(itertools.product(a, repeat=3)):
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