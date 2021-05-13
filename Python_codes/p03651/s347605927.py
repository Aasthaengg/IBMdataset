a,b = map(int, input().split())
c = list(map(int, input().split())) 
c.sort()
c.reverse() 
d = c[0]   
for i in range (1, a):
  while c[i] != 0:
    d , c[i] = c[i] , d % c[i]
if b > c[0]:
  print('IMPOSSIBLE')
else:
  print('POSSIBLE' if b%d == 0 else 'IMPOSSIBLE')