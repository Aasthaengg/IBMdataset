def euclidean(a,b):
  _ = a % b
  if _ == 0:
    return b
  else:
    while 1:
      if b % _ == 0 :
        break
      else:
        _ = b % _
    return _
  
A, B, K = map(int, input().split())
 
a = max(A, B)
b = min(A, B)
e = euclidean(a, b)
by = []
r = int(e ** (1 / 2))
 
for i in range(1, r + 1):
  if e % i == 0:
    by.append(i)
    j = e // i
    if j != i:
      by.append(j)
by.sort(reverse = True)
print(by[K - 1])