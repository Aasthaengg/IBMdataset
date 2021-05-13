s = ""
while True:
    try:
        s += input()
    except EOFError:
        break
s = s.lower()
d = dict()
for c in "abcdefghijklmnopqrstuvwxyz":
    d[c] = 0
for c in s:
    if c in "abcdefghijklmnopqrstuvwxyz":
        d[c] += 1
for c in "abcdefghijklmnopqrstuvwxyz":
    print(f"{c} : {d[c]}")
