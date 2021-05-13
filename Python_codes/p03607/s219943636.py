s = set()
for _ in range(int(input())):
    i = (int(input()))
    if i not in s:
        s.add(i)
    else:
        s.remove(i)
print(len(s))