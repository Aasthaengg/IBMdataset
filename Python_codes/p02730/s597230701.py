s = input()
n = len(s)
if s != s[::-1]:
    print("No")
else:
    t = s[:int((n - 1) / 2)]
    u = s[int((n + 1) / 2):]
    if t == t[::-1] and u == u[::-1]:
        print("Yes")
    else:
        print("No")