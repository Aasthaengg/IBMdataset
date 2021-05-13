S = input()
if S[0] == "A":
  count = 0
  for i in S[2:-1]:
    if i == "C":
      count += 1
  if count == 1:
    c = 0
    for i in S:
      if i.isupper():
        c += 1
    if c == 2:
      print("AC")
      exit()
print("WA")