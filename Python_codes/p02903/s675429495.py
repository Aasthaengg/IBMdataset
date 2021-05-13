h,w,a,b = map(int, input().split())

s = [['0' for j in range(w)] for i in range(h)]

for i in range(b):
  for j in range(a,w):
    s[i][j] = '1'

for i in range(b,h):
  for j in range(a):
    s[i][j] = '1'

for i in range(h):
  print (''.join(s[i]))
