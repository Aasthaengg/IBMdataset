a = input()
b = input()
n = max(len(a),len(b))

b = b.zfill(n)
a = a.zfill(n)

for i in range(n):
  if int(a[i])>int(b[i]):
    print("GREATER")
    exit()
  elif int(a[i])<int(b[i]):
    print("LESS")
    exit()

print("EQUAL")
