k = int(input())
q, r = divmod(k, 50)
L = [q+49]*50
for i in range(r):
  L[i] += 51-r
for i in range(r, 50):
  L[i] -= r
print(50)
print(*L)