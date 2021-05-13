N,A,B,C,D = map(int,input().split())
S = input()
A_start = True
if C < D:
  space1 = S[A-1:D]
  if ('##' in space1) != True:
    print('Yes')
  else:
    print('No')
else:
  space1 = S[A-1:C]
  space2 = S[B-2:D+1]
  if ('##' in space1) != True and ('...' in space2) == True:
    print('Yes')
  else:
    print('No')
