s = input()
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

for i in d.values():
    if i & 1 != 0:
        print("No")
        break
else:
    print("Yes")