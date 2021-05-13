a = list(map(str, input()))
b = []
for i in a:
    if i not in b:
        b.append(i)
if len(b) == 2:
    print("Yes")
else:
    print("No")