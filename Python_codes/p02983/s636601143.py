import sys
 
L, R = map(int, input().split())
 
if R-L >= 2019:
  print('0')
  sys.exit()
 
L = L % 2019
R = R % 2019
if L > R:
  print('0')
 
mmin = 2019
for i in range(L, R):
  for j in range(i+1, R+1):
    mmin = min(mmin, (i*j)%2019)
print(mmin)