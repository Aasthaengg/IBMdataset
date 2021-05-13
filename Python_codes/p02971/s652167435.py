N = int(input())
A = []
max1 = 0
max2 = 0
for i in range(N):
  a = int(input())
  A.append((a,i))
K = A.copy()
K.sort()
m1 = K[-1]
m2 = K[-2]
for i in range(N):
  if i == m1[1]:
    print(m2[0])
  else:
    print(m1[0])