N, M = input().split(' ')
N = int(N)
M = int(M)
min = 1
max = N
for i in range(M):
  l, m = input().split(' ')
  l = int(l)
  m = int(m)
  if min>m or max<l:
    print(0)
    break 
  if min < l:
    min = l
  if max > m:
    max = m
else:
  print(max-min+1)