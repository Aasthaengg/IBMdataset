S = int(input())

a = [0] * 2000
a[0] = 0
a[1] = 0
a[2] = 1
a[3] = 1
a[4] = 1
a[5] = 2

for i in range(6, S):
  k = 0
  for l in range(2, i-2):
    k += a[l]
  a[i] = 1 + k
  
p = a[S-1] % (10**9 + 7)
print(p)