H,W=map(int,input().split())
D={chr(code): 0 for code in range(ord('a'), ord('z') + 1)}
for i in range(H):
  A=list(input())
  for i in A:
    D[i]+=1
if H%2==0 and W%2==0:
  for i in D.values():
    if i%4!=0:
      print('No')
      exit()
  print('Yes')
elif H%2==1 and W%2==1:
  E=[]
  for i in D.values():
    if i%4!=0:
      E.append(i%4)
  E=sorted(E)
  a=H+W-1
  if H==1 or W==1:
    for i in range(a//2+1):
      if E==[1]+[2]*i:
        print('Yes')
        exit()
    print('No')
    exit()    
  if (a+1)//2 <len(E):
    print('No')
    exit()
  for i in range(a//2+2):
    if E==[1]+[2]*i:
      print('Yes')
      exit()
  print('No')
else:
  E=[]
  for i in D.values():
    if i%4!=0:
      E.append(i%4)
  E=sorted(E)
  if H%2==0:
    a=H
  else:
    a=W
  if a//2 <len(E):
    print('No')
    exit()
  for i in range(a//2+1):
    if E==[2]*i:
      print('Yes')
      exit()
  print('No')
