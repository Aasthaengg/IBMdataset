H, W = map(int, input().split())
N = int(input())
alist = [[a, i+1] for i, a in enumerate(map(int, input().split()))]
alist.sort()
drow_Order = []
for x in alist:
  for a in range(x[0]):
    drow_Order += [x[1]]
ans = ''
aaa = 0
for row in range(H):
  if row%2==0:
    ans = map(str, drow_Order[row*W:(row+1)*W])
  else:
    ans = map(str, reversed(drow_Order[row*W:(row+1)*W]))
  ans = ','.join(ans)
  print(ans.replace(',', ' '))