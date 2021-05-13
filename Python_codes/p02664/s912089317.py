t = list(input())
l = len(t)

for i in range(l):
    if t[i] == "?":
        t[i] = "D"
        print(t[i],end="")
    else:
        print(t[i],end="")