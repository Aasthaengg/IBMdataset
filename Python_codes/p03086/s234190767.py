a = list(input())

c = 0
m = 0

for x in a:
    if x in ["A", "C", "G", "T"]:
        c += 1
    else:
        m = max(m, c)
        c = 0

print(max(m, c))