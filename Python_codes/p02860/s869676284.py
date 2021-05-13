n = int(input())
S = input()
if n & 1:
  print("No")
else:
  if S[:n//2] == S[n//2:]:
    print("Yes")
  else:
    print("No")