N = int(input())
L = list(map(int, input().split()))
m = max(L)
o = sum(L) - m
if m < o:
  print("Yes")
else:
  print("No")