S = input()
a = 0
b = len(S) - 1
while 1:
  if S[a] == "A":
    break
  a += 1
while 1:
  if S[b] == "Z":
    break
  b -= 1
print(b - a + 1)