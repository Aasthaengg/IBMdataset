N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

button = [0] * N
button[0] = 1
next_button = 1
i = 0

while True:
  button[next_button - 1] = 2
  next_button = A[next_button - 1]
  if button[next_button - 1] == 2:
    print("-1")
    break
  elif next_button == 2:
    i += 1
    print(i)
    break
  else:
    button[next_button - 1] = 1
    i += 1

