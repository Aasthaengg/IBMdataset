int = int(input())
i=1
while i<=3:
  dev=int % 10
  if dev == 7:
    print("Yes")
    i=5
  int = int // 10
  i += 1
  if i==4:
    print("No")
