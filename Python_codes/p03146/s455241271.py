s = int(input())
t = []
t.append(s)
while True:
    if s % 2 == 0:
        s = s // 2
    else:
        s = s * 3 + 1
    t.append(s)
    if t.count(s) == 2:
        print(len(t))
        exit(0)