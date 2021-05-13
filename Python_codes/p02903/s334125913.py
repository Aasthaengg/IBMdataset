a,b,c,d=map(int,input().split())
for i in range(a):
  if i<d:
    print('1'*c+'0'*(b-c))
  else:
    print('0'*c+'1'*(b-c))