input()
A=list(map(int,input().split()))

def even(num, l):
    if num % 2 == 0:
        l.append(num)
        
B = []
for num in A:
    even(num, B)
    
C = []
for nn in B:
  if nn % 3 != 0 and nn % 5 != 0:
    C.append(nn)
    
if len(C) == 0:
  print('APPROVED')
else:
  print('DENIED')