s = input()
f = []
c = []
for i in range(len(s)):
    if s[i] == "F":
        f.append(i)
    elif s[i] == "C":
        c.append(i)
if f and c and (max(f)-min(c) > 0):
    print("Yes")
else:
    print("No")