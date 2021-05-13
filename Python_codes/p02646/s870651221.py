x,y = input().split()
q,w = input().split()
a =int(x)
b=int(y)
c= int(q)
d =int(w)
e =int(input())

if c-a >0:
  if c-a <=e*(b-d):
    print('YES')
   
  else:
    print('NO')
    
else:
  if a-c<=e*(b-d):
    print('YES')
   
  else:
    print('NO')