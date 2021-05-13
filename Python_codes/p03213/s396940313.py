n = int(input())
prime = [2]
for i in range(3,n+1,2):
  for j in prime:
    if i % j == 0:
      break
    elif i**0.5 < j:
      prime.append(i)
      break
di = dict(zip(prime,[0]*len(prime)))
for i in range(1,n+1):
  for j in prime:
    if i == 1:
      break
    c = 0
    while i % j == 0:
      i = i//j
      c += 1
    di[j] += c
a = len([i for i in di.values() if i >= 74])
b = len([i for i in di.values() if i >= 24])
c = len([i for i in di.values() if i >= 14])
d = len([i for i in di.values() if i >= 4])
e = len([i for i in di.values() if i >= 2])
print(a + b*(e-1) + c*(d-1) + d*(d-1)*(e-2)//2)