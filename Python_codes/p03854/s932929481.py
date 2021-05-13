s = input()
n = len(s)

s = "".join(reversed(list(s)))
while n:
    if s.startswith("maerd"):
        n -= 5
        s = s[5:]
    elif s.startswith("remaerd"):
        n -= 7
        s = s[7:]
    elif s.startswith("esare"):
        n -= 5
        s = s[5:]
    elif s.startswith("resare"):
        n -= 6
        s = s[6:]
    else:
        break
print("YES" if n == 0 else "NO")
