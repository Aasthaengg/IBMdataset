def check(a):
  for i in range(int(len(a)/2)):
    if a[i]!=a[-(i+1)]:
       return False
  return True
 
S=input()
if check(S):
  a=S[0:int(len(S)/2)]
  b=S[int(len(S)/2)+1:len(S)]
  if check(a) and check(b):
    print('Yes')
  else:
    print('No')
else:
    print('No')