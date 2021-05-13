n = int(input())
same = 0
for _ in range(n):
  d1, d2 = map(int, input().split())
  if d1 == d2:
    same += 1
  else:
    same = 0
  if same == 3:
    print("Yes")
    break
else:
  print("No")