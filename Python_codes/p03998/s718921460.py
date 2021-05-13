A = []
for i in range(3):
  a = input()
  A.append(a)
x = 0
while 1:
  if len(A[x]) == 0:
    print(chr(65 + x))
    break
  s = A[x][0]
  A[x] = A[x][1:]
  x = ord(s) - 97