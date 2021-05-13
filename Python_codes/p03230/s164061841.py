n=int(input())
l=[i*(i-1)//2 for i in range(2,450)]
if n in l:
  print('Yes')
  k=l.index(n)+1
  print(k+1)
  x=[[k] for _ in range(k+1)]
  p=1
  for i in range(k):
    for j in range(k-i):
      x[i].append(p+j)
      x[i+j+1].append(p+j)
    p=p+k-i
  for i in x:
    print(*i)
else:
  print('No')