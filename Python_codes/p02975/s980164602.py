from collections import Counter
def check():
  N = int(input())
  A = list(map(int, input().split()))
  if N%3 in [1,2]:
    if A!=[0]*N:
      return 'No'
    return 'Yes'
  c = Counter(A)
  if len(c)==1:
    if c[0]==0:
      return 'No'
    return 'Yes'
  if len(c)==2:
    if c[0]!=N//3:
      return 'No'
    return 'Yes'
  if len(c)==3:
    lis = []
    for k,v in c.items():
      if v!=N//3:
        return 'No'
      lis.append(k)
    if lis[0]^lis[1]==lis[2]:
      return 'Yes'
  return 'No'
print(check())