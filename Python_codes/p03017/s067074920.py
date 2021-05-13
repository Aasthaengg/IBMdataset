N, A, B, C, D = (int(i) for i in input().split())  
S = input()

bef = ''
row_dot_max = 0
count = 0
for i, s in enumerate(S):
  if bef == '#' and s == '#' and i > A and i <= max(C,D)-2:
    print('No')
    exit()
  
  if s == '.' and i >= B-2 and i <= D:
    count += 1
  else:
    row_dot_max = max(row_dot_max, count)
    count = 0
  bef = s

row_dot_max = max(row_dot_max, count)
if C > D:
  if row_dot_max >= 3:
    print('Yes')
  else:
    print('No')
else:
  print('Yes')