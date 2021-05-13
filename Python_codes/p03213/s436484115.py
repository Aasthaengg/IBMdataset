n = int(input())
def is_p(k):
  for i in range(2,int(k**0.5)+1):
    if k%i == 0:
      return False
  return True
p = []
for i in range(2,n+1):
  if is_p(i):
    p.append(i)
l = len(p)
q =[0]*l
for i in range(2,n+1):
  for j in range(l):
    if i == 1:
      break
    while i%p[j] == 0:
      q[j] += 1
      i /= p[j]
c = 0
for qi in q:
  if qi >= 74:
    c += 1
o2 = 0
o4 = 0
o14 = 0
o24 = 0
for qi in q:
  if qi >= 24:
    o24 += 1
  elif qi >= 14:
    o14 += 1
  elif qi >= 4:
    o4 += 1
  elif qi >= 2:
    o2 += 1
c += o24*(o2+o4+o14+o24-1)
c += (o14+o24)*(o4+o14+o24-1)
c += (o2+o4+o14+o24-2)*(o4+o14+o24)*(o4+o14+o24-1)//2  
print(c)