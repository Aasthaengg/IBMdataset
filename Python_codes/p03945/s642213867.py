s = input()
S = []
b = ""
for i in s:
  if b == "":
    S.append(i)
    b = i
  elif b == i: continue
  else:
    S.append(i)
    b = i
print(len(S)-1)