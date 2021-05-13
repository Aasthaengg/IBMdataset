N = int(input())

for i in range(N):
  temp = int(input())
  if temp%2 == 0:
    continue
  else:
    print("first")
    exit()
print("second")