o = input()
e = input()

pw = [""] * (len(o)+len(e))

for i in range(len(o)):
  pw[2*i] = o[i]
for i in range(len(e)):
  pw[2*i+1] = e[i]
print("".join(pw))