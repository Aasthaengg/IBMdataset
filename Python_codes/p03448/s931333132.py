A = int(input())
B = int(input())
C = int(input())
X = int(input())

pat_list = []
for a in range(A + 1):
  for b in range(B + 1):
    for c in range(C + 1):
      price = 500 * a + 100 * b + 50 * c
      pat_list.append(price)
print(pat_list.count(X))