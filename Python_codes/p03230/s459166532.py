N = int(input())

for i in range(10 ** 5) :
  if i * (i + 1) // 2 == N :
    print('Yes')
    print(i + 1)
    ret = [[] for _ in range(i + 1)]
    cur = 1
    for j in range(i + 1) :
      for _ in range(i - j) :
        ret[j].append(cur)
        cur += 1
    for j in range(1, i + 1) :
      for k in range(j) :
        ret[j].append(ret[k][i-j])
    for j in range(i + 1) :
      print(i, *ret[j])
    
    break
else :
  print('No')
