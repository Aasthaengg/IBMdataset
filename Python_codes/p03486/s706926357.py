s = sorted(list(input()))
t = sorted(list(input()), reverse=True)

s = "".join(s)
t = "".join(t)

if s == t:
    print("No")
else:
    l = sorted([s,t])
    if l[0] == s:
        print("Yes")
    else:
        print("No")