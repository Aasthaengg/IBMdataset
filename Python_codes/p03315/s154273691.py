j = {
    "-":-1,
    "+":1
    }
l =input()
s = 0
for i in range(len(l)):
  s += j[l[i]]
print(s)
