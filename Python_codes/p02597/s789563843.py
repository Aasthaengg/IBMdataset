N = int(input())
a = input()
wc = int(0)
rc = int(0)
c = int(0)

for i in range(N):
  if a[i] == "W":
    wc += 1
  else:
    rc += 1

if rc == 0:
  print("0")
else:
  for i in range(rc):
    if a[i] == "W":
      c += 1
  print(c)