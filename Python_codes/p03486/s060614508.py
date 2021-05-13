s = list(input())
t = list(input())

s = sorted(s)
t = sorted(t, reverse=True)

sstr = "".join(s)
tstr = "".join(t)


if tstr > sstr:
    print("Yes")
else:
    print("No")