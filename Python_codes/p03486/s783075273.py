s = input()
t = input()

if (len(s) < len(t)) and (s == t[:len(s)]):
    print("Yes")
else:
    s = sorted(list(s))
    t = sorted(list(t))

    if t[-1] > s[0]:
        print("Yes")
    else:
        print("No")