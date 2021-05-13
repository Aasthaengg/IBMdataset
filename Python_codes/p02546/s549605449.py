a = input()
b = [str(c) for c in a]

if b[-1] == "s":
  b.append("es")
  
else:
  b.append("s")

print(''.join(b))