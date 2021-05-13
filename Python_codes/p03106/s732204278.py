A, B, K = list(map(int, input().split()))
arr = []

for i in range(1,101):
  if A%i == 0 and B%i == 0:
    arr.append(i)
print (arr[-K])
