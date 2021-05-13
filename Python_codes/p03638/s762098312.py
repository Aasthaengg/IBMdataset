h, w = map(int, input().split())
n = int(input())
a = [int(i) for i in input().split()]
k = 1
r = a[0]
for i in range(h):
  tmp = []
  for j in range(w):
    if r==0:
      r = a[k]
      k += 1
    tmp.append(k)
    r -= 1
  if i%2==1:
    tmp = tmp[::-1]
  print(*tmp)