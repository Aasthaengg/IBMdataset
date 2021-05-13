import copy

s = input()
x,y = map(int,input().split())

X = []
Y = []
l = 0
f = -1
xinit = 0
A = s + 'T'
for a in A:
  if a == 'T':
    if f == -1:
      xinit = l
      f = 1
    elif f == 0:
      X.append(l)
      f = 1
    else:
      Y.append(l)
      f = 0
    l = 0
  else:
    l += 1

def pattern(P,init=0):
  Q = set()
  Q.add(init)
  for p in P:
    QQ = set()
    for q in Q:
      QQ.add(q+p)
      QQ.add(q-p)
    Q = copy.copy(QQ)
  return Q

XX = pattern(X,xinit)
YY = pattern(Y)
#print(XX,YY)
if x in XX and y in YY:
  print('Yes')
else:
  print('No')