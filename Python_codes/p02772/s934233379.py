import sys
n = int(input())
A = list(map(int, input().split()))
for a in A:
  if a%2 == 0:
    if (a%3 == 0) or (a%5 == 0):
      pass
    else:
      print("DENIED")
      sys.exit()
print("APPROVED")