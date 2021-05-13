N = int(input())
D, X = input().split(' ')
D = int(D)
X = int(X)
count = 0
for i in range(N):
  a = int(input())
  count += 1
  for j in range(1, D, 1):
    if (D - 1) - a * j >= 0:
      count += 1   
print(count + X)