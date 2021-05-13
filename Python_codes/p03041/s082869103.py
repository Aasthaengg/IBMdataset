n, k = map(int, input().split())
k = k-1
s = input()

for i in range(n):
  if i != k:
    print(s[i], end="")
  else:
    if s[k] == "A":
      print("a", end="")
    elif s[k] == "B":
      print("b", end="")
    elif s[k] == "C":
      print("c", end="")