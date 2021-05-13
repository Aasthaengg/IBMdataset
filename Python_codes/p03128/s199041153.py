def is_big(x = [0]*10, y = [0]*10):
    if sum(x) > sum(y):
        return True
    if sum(x) < sum(y):
        return False
    for i in range(0,10)[::-1]:
        if x[i] > y[i]:
            return True
        if y[i] > x[i]:
            return False
    return True
  
n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
#print(a)
d = [0]*8
b = []
L1 = [1,7,4,2,3,5,6,9,8]
L2 = [2,3,4,5,5,5,6,6,7]
for i in range(9):
  if L1[i] in a:
    d[L2[i]] = L1[i]
    if L2[i] not in b:
      b.append(L2[i])
#print(d)
#print(b)
p = []
for i in range(n+1):
  p.append([-1,0,0,0,0,0,0,0,0,0])
  
p[0][0] = 0
for i in range(1,n+1):
  for t in b:
    if i-t <0 or p[i-t][0] == -1: 
      continue
    q = p[i-t][:]
    q[d[t]] += 1
    if is_big(q,p[i]):
      p[i] = q

a = ""
for i in range(10)[::-1]:
  a += str(i)*p[n][i]
print(a)