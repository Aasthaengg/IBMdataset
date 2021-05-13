n = int(input())
s = [input() for _ in range(n)]

ab, a, b, b_a = 0, 0, 0, 0
for i in s:
  ab += i.count('AB')
  if i[-1] == 'A':
    a += 1
  if i[0] == 'B':
    b += 1
  if i[0] == 'B' and i[-1] == 'A':
    b_a +=1

a -= b_a
b -= b_a
if a == 0 and b == 0:
  print(ab + max(b_a-1, 0))
else:
  print(ab + min(a, b) + b_a)