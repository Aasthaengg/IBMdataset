N = int(input())
 
def make_devision(n):
  lst = []
  for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
      lst.append(i)
      if i != n // i:
        lst.append(n // i)
  return lst
 
def calc(n, k):
  if n % k == 0:
    return calc(n // k, k)
  elif n < k:
    return n
  else:
    return calc(n % k, k)
 
ans = make_devision(N-1)
 
for i in make_devision(N):
  if i == 1:
    continue
  if calc(N, i) == 1:
    ans.append(i)
    
print(len(ans)-1)