K = int(input())
A, B = map(int, input().split(" "))

if B // K > (A-1) // K:
  print("OK")
else:
  print("NG")