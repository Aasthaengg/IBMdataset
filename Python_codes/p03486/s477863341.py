s = input()
t = input()
_s = "".join(sorted(s))
_t = "".join(sorted(t)[::-1])

if _s < _t:
    print("Yes")
else:
    print("No")
