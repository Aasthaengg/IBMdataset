t = list(str(input()))
if len(t) == 1:
    if t[0] == "?":
        print("D")
        exit()
for i in range(1,len(t)):
    if t[i] == "?":
        if t[i-1] == "P":
            t[i] = "D"
        elif t[i-1] == "?":
            t[i-1] = "P"
            t[i] = "D"
for i in range(len(t)-1):
    if t[i] == "?":
        if t[i+1] == "D":
            t[i] = "P"
        elif t[i+1] == "P":
            t[i] = "D"
if t[-1] == "?":
    t[-1] = "D"
ans = "".join(t)
print(ans)