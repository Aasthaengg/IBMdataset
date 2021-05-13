d = {}

for i in range(int(input())):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

for i in range(int(input())):
    t = input()
    if t in d:
        d[t] -= 1

print(max(0, max(i for i in d.values())))