s = input()
start = 2 if len(s) % 2 == 0 else 1
for i in range(start, len(s), 2):
    t = s[:-i]
    mid = len(t) // 2
    if t[:mid] == t[mid:]:
        print(len(t))
        break