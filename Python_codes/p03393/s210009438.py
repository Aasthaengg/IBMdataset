s = input()

def set_char(data, c):
    for i in range(26):
        ret = chr(ord("a") + i)
        if ret not in data and ret > c:
            return ret

if len(s) < 26:
    data = set(s)
    for i in range(26):
        c = set_char(data, "")
    print(s + c)
else:
    i = len(s) - 1
    while i != 0 and s[i - 1] > s[i]:
        i -= 1
    if i == 0:
        print(-1)
    else:
        data = set(s[: i - 1])
        c = set_char(data, s[i - 1])
        print(s[: i - 1] + c)
