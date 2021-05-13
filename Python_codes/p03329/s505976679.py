N = int(input())
a = N

for n in range(N+1):
  c = 0
  t = n
  while t>0:
    c+=t%6
    t//=6
  t = N-n
  while t>0:
    c+=t%9
    t//=9
  a = min(a,c)
  
print(a)