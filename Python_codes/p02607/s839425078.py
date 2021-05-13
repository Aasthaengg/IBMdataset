N = int(input())
a = list(map(int, input().split()))
count = 0

for i, number in enumerate(a, 1):
  if i % 2 != 0 and number % 2 != 0:
    count += 1

print(count)