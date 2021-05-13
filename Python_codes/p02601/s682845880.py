A,B,C = [ int(n) for n in input().split() ]
K = int(input())

ptrn = ["A","B","C"]
for k in range(1,K):
  plen = len(ptrn)
  for i in range(plen) :
    wptrn = ptrn.pop(0)
    ptrn.append( wptrn + "A") 
    ptrn.append( wptrn + "B")
    ptrn.append( wptrn + "C")
    
flg = False    
for p in ptrn :
  plist = list(p)
  a = A
  b = B
  c = C
  for q in plist:
    if q == 'A':
      a *= 2
    elif q == 'B':
      b *= 2
    else:
      c *= 2
  if a < b and b < c:
    flg = True
    
print("Yes" if flg else "No")