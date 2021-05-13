
n = input()
a = []
for i in range(len(n)):
  if n[i] == "1":
    a.append("9")
  elif n[i] == "9":
    a.append("1")
  else:
    a.append(n[i])
print("".join(a))


