MM = input().split()
A = int(MM[0])
B = int(MM[1])
total = 1
count = 0
while total < B:
  total += A-1
  count += 1
print(count)