s = input()

a = []

for i in s:
    if i == "C" or i == "F":
        a.append(i)
a = "".join(a)
if a.count("CF") > 0:
    print("Yes")
else:
    print("No")