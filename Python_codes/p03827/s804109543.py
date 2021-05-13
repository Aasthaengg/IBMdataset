n = int(input())
s = list(input())

x=0
a = [0]
for i in range(len(s)):
  if s[i] == "I":
    x += 1
    a.append(x)
  else:
    x += -1
    a.append(x)

print(max(a))