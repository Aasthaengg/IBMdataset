n = input()
s = []
for i in range(len(n)):
    if n[i] == "1":
        s.append("9")
    else:
        s.append("1")
print(*s, sep="")