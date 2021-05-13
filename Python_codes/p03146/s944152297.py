s = int(input())
a = s
A = []
A.append(s)
count = 0

while True:
  count += 1
  if a % 2 == 0:
    a = a/2
  else:
    a = 3*a + 1
  if a in A:
    break
  A.append(a)
  
print(count+1)