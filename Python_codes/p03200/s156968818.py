r = input()

s = 0
c = 0

for i in range(len(r)):
  if r[i] == "W":
    s += i - c
    c += 1

print(s)