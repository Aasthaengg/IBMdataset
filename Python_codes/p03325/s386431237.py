N = int(input())
a = list(map(int, input().split()))
odd = [i for i in a if i % 2 != 0]
even = [i for i in a if i % 2 == 0]
result = []
count = 0
while True:
  for i in even:
    if i != 0 and i % 2 == 0:
      result.append(i//2)
      count += 1
  if not result:
    print(count)
    exit()
  even = result
  result = []