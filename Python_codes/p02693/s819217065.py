k = int(input())
a, b = map(int, input().split())

flag = False

if a <= int(b / k) * k:
  print("OK")
else:
  print("NG")