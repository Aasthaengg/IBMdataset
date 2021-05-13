p = input()
s = []
for i in range(len(p)):
    s.append(p[i])
if len(s) == 3:
    s.reverse()
print("".join(s))