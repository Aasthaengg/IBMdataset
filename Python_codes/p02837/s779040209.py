N = int(input())
A = []
L = []
for i in range(N):
  a = int(input())
  A.append(a)
  tmp = []
  for i in range(a):
    tmp.append(list(map(int, input().split())))
  L.append(tmp)

ans = 0
for i in range(1, 2**N):
  tmp = [-1] * N
  flag = True
  d = []
  for j in range(N):
    if (i>>j) & 1:
      if tmp[j] == 0:
        flag = False
        break
      tmp[j] = 1
      l = L[j]
      for k in range(len(L[j])):
        p, t = l[k][0], l[k][1]
        if tmp[p-1] < 0:
          tmp[p-1] = t
        elif tmp[p-1] != t:
          flag = False
          break
      if flag == False:
        break
    else:
      d.append(j)
  for m in range(len(d)):
    n = d[m]
    if tmp[n] == 1:
      flag = False
      break
  if flag:
    ans = max(ans, tmp.count(1))
print(ans)