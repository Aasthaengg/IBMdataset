o = str(input())
e = str(input())
s = []
for i in range(len(e)):
    s.append(o[i])
    s.append(e[i])
if len(o) > len(e):
    s.append(o[-1])
print(*s, sep = "")