n = int(input())
s = set()
for i in range(n):
    a = int(input())

    if a not in s:
        s.add(a)
    else:
        s.remove(a)

print(len(s))
