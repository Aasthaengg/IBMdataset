S = input()
a = []
for s in S:
  if s in a:
    print("no")
    exit()
  else:
    a.append(s)

print("yes")