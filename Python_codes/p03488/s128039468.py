s = input()
l = len(s)
s = 'F' + s
x,y = map(int,input().split())
raw = [1]
for i in range(1,l+1):
  if s[i] == 'F':
    if s[i-1] == 'F':
      raw[-1] += 1
    else:
      raw.append(1)
  if s[i] == 'T':
    if s[i-1] == 'T':
      raw.append(0)
l2 = len(raw)
a = []
b = []
for i in range(l2):
  if i == 0:
    x -= raw[i]-1
  elif i % 2 == 0:
    a.append(raw[i])
  else:
    b.append(raw[i])
#print(raw)
#print(a,x)
#print(b,y)
nowa = {0}
for aa in a:
  lasta = nowa
  nowa = set()
  for aaa in lasta:
    nowa.add(aaa+aa)
    nowa.add(aaa-aa)
nowb = {0}
for bb in b:
  lastb = nowb
  nowb = set()
  for bbb in lastb:
    nowb.add(bbb+bb)
    nowb.add(bbb-bb)
#print(nowa,nowb)
#print(x,y)
if x in nowa and y in nowb:
  print('Yes')
else:
  print('No')