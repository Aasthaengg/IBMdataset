n = int(input())
s = input()
d = 0
a = []
for i in s:
    if i == "I":
        d += 1
        a.append(d)
    else:
        d -= 1
        a.append(d)
if max(a) <= 0:
    print(0)
else:
    print(max(a))