from collections import deque
d = deque()
X = input()
for c in X:
    if d:
        last = d.pop()
        if last == "S" and c == "T":
            pass
        else:
            d.append(last)
            d.append(c)
    else:
        d.append(c)
print(len(d))
