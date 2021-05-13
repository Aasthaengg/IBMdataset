n, k, s = map(int, input().split())

for i in range(k):
  print(s, end=" ")
if s == 1000000000:
  for i in range(n-k):
    print(1, end=" ")
else:
  for i in range(n-k):
    print(1000000000, end=" ")

print()