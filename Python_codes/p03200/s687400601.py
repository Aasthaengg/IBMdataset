S = list(input())
count = 0
valueA = 0
for i in range(len(S)):
  if S[i] == 'B':
    count += 1
    valueA += i

valueB = 0
for i in range(count):
  valueB += (len(S) - 1 - i)
  
print(valueB - valueA)