n=(int)(input())
a=list(map(int, input().split(" ")))
for i in range(len(a) - 1, 0, -1):
  if a[i] < a[i - 1]:
    a[i - 1] -= 1
  if a[i] < a[i - 1]:
    print("No")
    break
else:
  print("Yes")