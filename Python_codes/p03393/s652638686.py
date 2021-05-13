import collections
s = input()


cnt = collections.Counter(s)
used = set(cnt.keys())
c = -1
if len(used) < 26:
    for i in range(26):
        if not chr(i+ord("a")) in used:
            c = chr(i+ord("a"))
            break
if c != -1:
    print(s+c)
else:
    if s == "zyxwvutsrqponmlkjihgfedcba":
        print("-1")
        exit()
    i = 25
    while i > 1 and s[i-1] > s[i]:
        i -= 1
    lused = sorted(s[i-1:])
    print(s[:i-1]+lused[lused.index(s[i-1])+1])
