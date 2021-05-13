s = list(input())
while s:
    s = s[:-1]
    sl = len(s)
    if sl%2 == 0:
        s1 = s[0:sl//2]
        s2 = s[sl//2:]
        if s1 == s2:
            print(sl)
            break