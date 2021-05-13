n,k,q = list(map(int,input().split()))
point = [k-q] * n

for i in range(q):
  tmp = int(input()) - 1
  point[tmp] += 1

for i in range(n):
  if point[i] >= 1:
    print('Yes')
  else:
    print('No')
