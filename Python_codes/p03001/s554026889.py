a = list(map(int,input().split()))
S = a[0]*a[1]/2
if a[0]/2 == a[2] and a[1]/2 == a[3]:
  print(S,1)
else:
  print(S,0)

