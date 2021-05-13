a,b,c = map(int, input().split())
numbers = []
count = 0

while True:
  if a > b:
    break
  numbers.append(a)
  a += 1

for i in range(len(numbers)):
  if c % numbers[i] == 0:
    count += 1

print(count)
