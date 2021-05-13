N = int(input())
for _ in range(3):
  if N%10==7:
    print("Yes")
    break
  N //=10
else:
  print("No")