x = input()
s = 0
t = 0
for i in range(len(x)):
    if x[i] == "T":
        s = max(0, s-1)
    else:
        s += 1
    if x[-i-1] == "S":
        t = max(0, t -1)
    else:
        t += 1
print(s+t)
