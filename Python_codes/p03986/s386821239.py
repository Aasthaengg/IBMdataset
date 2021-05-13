from collections import deque
d = deque()
X = input()
for c in X:
    d.append(c)
    while len(d) >= 2:
        new = d.pop()
        last = d.pop()
        if last == "S" and new == "T":
            continue
        else:
            d.append(last)
            d.append(new)
            break
print(len(d))