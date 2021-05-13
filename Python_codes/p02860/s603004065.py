N = int(input())
if N%2 == 1:
  print("No")
  exit()

S = str(input())
mid = N//2
s1 = S[:mid]
s2 = S[mid:]
if s1 == s2:
  print("Yes")
else:
  print("No")