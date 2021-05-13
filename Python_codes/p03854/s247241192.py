A = input()
A = A[::-1]
divide = [i[::-1] for i  in ["dream", "dreamer", "erase", "eraser"]]

flag = 1
while flag and A:
  flag = 0
  for word in divide:
    if A.startswith(word):
      A = A[len(word):]
      flag = 1

if len(A) == 0:
  print('YES')
else:
  print('NO')