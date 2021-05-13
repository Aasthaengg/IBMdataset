d, n = map(int, input().split())
arr = []
i = 1
while len(arr) != n:
  if 100 ** d * i % 100 ** (d + 1) != 0:
    arr.append(100 ** d * i)
  i += 1
print(arr[-1])