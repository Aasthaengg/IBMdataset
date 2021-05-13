n, a, b = map(int,input().split())
*p, = map(int,input().split())
l = []
#print(p)
for i in range(1,n):
  w = (p[i]-p[i-1])*a 
  if w >= b:
    l.append(b)
  else:
    l.append(w)
#print(l)
print(sum(l))