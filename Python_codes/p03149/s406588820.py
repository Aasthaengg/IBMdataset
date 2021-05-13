n= map(int, input().split())
n = sorted(list(set(n)))
if n[0]==1 and n[1]==4 and n[2]==7 and n[3]==9:
  print('YES')
else:
  print('NO')