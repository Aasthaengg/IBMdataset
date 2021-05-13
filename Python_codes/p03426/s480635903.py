H, W, D, *L = map(int, open(0).read().split())
A = L[:W*H]
Q = L[H*W]
inf = []
for l,r in zip(*[iter(L[H*W+1:])]*2):
  inf += [(l,r)]
dic = {A[i*W+j]:(i,j) for i in range(H) for j in range(W)}
ls = [[] for i in range(D)]
for i in range(D):
  s = i if i!=0 else D
  ls[i].append(0)
  m = s
  n = s
  while True:
    n += D
    if H*W<n:
      n = s
    px, py = dic[m]
    x, y = dic[n]
    ls[i].append(ls[i][-1]+abs(px-x)+abs(py-y))
    m = n
    if m==s:
      break
for l, r in inf:
  i = l%D
  if i==0:
    il = (l-D)//D
    ir = (r-D)//D
  else:
    il = (l-i)//D
    ir = (r-i)//D
  if l<r:
    print(ls[i][ir] - ls[i][il])
  elif l>r:
    print(ls[i][-1]-ls[i][il]+ls[i][ir])
  else:
    print(0)