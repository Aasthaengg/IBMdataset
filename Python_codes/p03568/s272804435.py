n = int(input())
A = list(map(int, input().split()))

count = 1
for a in A:
  count *= 2 if a % 2 == 0 else 1
print(3 ** n - count)