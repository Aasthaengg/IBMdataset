A, B = map(int, input().split())

time = A + B
if time >= 24:
  time = time - 24
print(time)