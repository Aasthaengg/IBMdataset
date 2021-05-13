N,A,B = map(int,input().split())
maxN,minN = 0,0

if N >= A + B:
  minN = 0
  maxN = min([A,B])
else:
  minN = A + B - N
  maxN = min([A,B])
  
print('{} {}'.format(maxN,minN))
