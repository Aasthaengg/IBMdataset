from collections import Counter
def check():
  H, W = map(int, input().split())
  A = ''
  for i in range(H):
    A += input()
  c = Counter(A)
  if H%2==0:
    if W%2==0:
      for v in c.values():
        if v%4!=0:
          return 'No'
      return 'Yes'
    cnt = 0
    for v in c.values():
      if v%2==1:
        return 'No'
      if v%4==2:
        cnt += 1
        if cnt>H//2:
          return 'No'
    return 'Yes'
  if W%2==0:
    cnt = 0
    for v in c.values():
      if v%2==1:
        return 'No'
      if v%4==2:
        cnt += 1
        if cnt>W//2:
          return 'No'
    return 'Yes'
  one,two = 0,0
  for v in c.values():
    if v%2==1:
      one += 1
    if v%4==2:
      two += 1
    if one>1 or two>W//2+H//2:
      return 'No'
  return 'Yes'
print(check())