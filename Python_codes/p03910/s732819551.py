n = int(input())
l, r = 0, n**2
while r-l > 1:
  k = (r+l)//2
  if k*(k+1)//2 < n:
    l = k
  else:
    r = k

if n == 1:
  r = 1

key = []
for i in range(r, 0, -1):
  if n-i >= 0:
    key.append(i)
    n -= i
    if not n:
      break

key.reverse()
for value in key:
  print(value)