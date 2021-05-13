H,W,A,B = map(int,input().split())
if A>=W or B>=H:
  print('No')
else:
  [print(''.join(['0']*(W-A)+['1']*A)) for _ in range(B)]
  [print(''.join(['1']*(W-A)+['0']*A)) for _ in range(H-B)]