n, a, b, c, d = map(int, input().split())
S = input()
if c < d:
  for i in range(a-1, d-1):
    if S[i] == "#" and S[i+1] == "#":
      print("No")
      exit()
  print("Yes")
else:
  for i in range(a-1, d-1):
    if S[i] == "#" and S[i+1] == "#":
      print("No")
      exit()
  for i in range(b-1, min(d, n-1)):
    if S[i-1] == "." and S[i] == "." and S[i+1] == ".":
      print("Yes")
      exit()
  print("No")