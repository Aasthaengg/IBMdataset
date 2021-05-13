N = int(input())
S = list(map(int,input().split(" ")))

dec = max(S)
total = 0

for i in S:
  total += i
total -= dec
if total > dec:
  print("Yes")
else:
  print("No")