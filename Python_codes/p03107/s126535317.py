S = input()

zeros = 0
ones = 0

for char in S:
  if char == '0':
    zeros += 1
  else:
    ones += 1
    
print(min(zeros, ones) * 2)