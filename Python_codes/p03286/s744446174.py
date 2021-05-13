N = int(input())
ans = 0

def F(N):
  if(N == 0):
    return ''
  
  if(N % 2 == 0):
    return F(N//-2) + '0'
  else:
    return F((N-1)//-2) + '1'

if(N == 0):
  print(0)
else:
  print(F(N))