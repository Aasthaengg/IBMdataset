n, m = map(int, input().split())
s_li_ = []
c_li_ = []

for _ in range(m):
  s, c = map(int, input().split())
  s_li_.append(s)
  c_li_.append(c)

def func(n, m, s_li, c_li):
  if m==0:
    if n==1:
      return 0
    else:
      return 10**(n-1)
  
  if n==1:
    if (s_li[0]==1) & (c_li[0]==0):
      return 0
  
  for i in range(10**(n-1), 10**n):
    cnt = 0
    for s, c in zip(s_li, c_li):
      if str(i)[s-1] == str(c):
        cnt+=1
    if cnt==m:
      return i
    
  return -1

print(func(n, m, s_li_, c_li_))
