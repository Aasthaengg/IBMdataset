import math

li=[int(input()) for _ in range(5)]
m,last,ans,lm=10,li[0],0,0

for i in range(5):
  l = li[i]
  if 0 < l % 10 < m :
    m = l % 10
    last = l
    lm = i

for i in range(5):
  l=li[i]
  if l == last and i == lm:
    ans += l
  else:
    ans += math.ceil(l/10)*10
    
print(ans)