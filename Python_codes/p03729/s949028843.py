Tmp = []
Tmp = input().rstrip().split(' ')

S1 = Tmp[0]
S2 = Tmp[1]
S3 = Tmp[2]

if S1[-1]==S2[0] and S2[-1]==S3[0]:
  print('YES')
else:
  print('NO')

