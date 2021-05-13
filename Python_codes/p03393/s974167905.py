s = input()
t = set(list(s))
n = len(s)
al={chr(ord('a') + i) for i in range(26)}
if n != 26:
    p = al - t
    p = list(p)
    p.sort()
    print(s + p[0])
elif n == 26:
    if s == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        now = s[25]
        p = []
        for i in reversed(range(26)):
            if ord(now) <= ord(s[i]):
                p.append(now)
                now = s[i]
            elif ord(now) > ord(s[i]):
                p.append(now)
                print(s[:i],end="")
                q = []
                for j in p:
                    if ord(s[i]) < ord(j):
                        q.append(ord(j))
                print(chr(min(q)))
                exit()