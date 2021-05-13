import math

X = int(input())

ans_list = []

for i in range(2, int(math.sqrt(X)) + 1, 1):
  j = 1
  while 1:
    if i ** j <= X:
      j += 1
    else:
      ans_list.append(i ** (j - 1))
      break
else:
  if X == 1:
    print(1)
  else:
    print(max(ans_list))