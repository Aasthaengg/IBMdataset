s=str(input())

def solve(s):
  if s.find("AA")!=-1:
    return False
  if s.find("KIH")==-1:
    return False
  t=s.replace('A','')
  return t=='KIHBR'

if solve(s):
  print('YES')
else:
  print('NO')