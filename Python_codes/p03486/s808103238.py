s = [x for x in input()]
t = [x for x in input()]
s = sorted(s)
t = sorted(t,reverse=True)
s = "".join(s)
t = "".join(t)
print("Yes" if s<t else "No")
