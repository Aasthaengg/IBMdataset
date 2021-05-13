N = int(input())
i = 0
f = 0
while i <= N:
  if (N - i) % 7 == 0:
    print("Yes")
    f = 1
    break
  i += 4
if f == 0:
  print("No")