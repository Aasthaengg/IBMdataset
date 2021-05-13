s = input()
x, y = map(int, input().split())
a = []
b = []
c = 0
n = 0
for i in range(len(s)):
  if s[i]=='F':
    n += 1
  else:
    if c%2==0:
      a += [n]
    else:
      b += [n]
    c += 1
    n = 0
if s[-1]=='F':
  if c%2==0:
    a += [n]
  else:
    b += [n]
sa = sum(a)
sb = sum(b)
dpa1 = [0]*(2*sa+1)
dpa2 = [0]*(2*sa+1)
dpb1= [0]*(2*sb+1)
dpb2 = [0]*(2*sb+1)
dpa1[sa] = 1
dpb1[sb] = 1
if len(a)>0:
  if sa-a[0]<abs(x-a[0]) or sb<abs(y):
    print('No')
    import sys
    sys.exit()
else:
  if sa<abs(x) or sb<abs(y):
    print('No')
    import sys
    sys.exit()

if len(a)%2==0:
  A = dpa1
else:
  A = dpa2
if len(b)%2==0:
  B = dpb1
else:
  B = dpb2

for i in range(len(a)):
  c = a[i]
  if i%2==0:
    for j in range(2*sa+1):
      if dpa1[j]==1:
        dpa1[j] = 0
        dpa2[j-c] = 1
        dpa2[j+c] = 1
  else:
    for j in range(2*sa+1):
      if dpa2[j]==1:
        dpa2[j] = 0
        dpa1[j-c] = 1
        dpa1[j+c] = 1
for i in range(len(b)):
  c = b[i]
  if i%2==0:
    for j in range(2*sb+1):
      if dpb1[j]==1:
        dpb1[j] = 0
        dpb2[j-c] = 1
        dpb2[j+c] = 1
  else:
    for j in range(2*sb+1):
      if dpb2[j]==1:
        dpb2[j] = 0
        dpb1[j-c] = 1
        dpb1[j+c] = 1

if A[x+sa]==1 and B[y+sb]==1:
  print('Yes')
else:
  print('No')
