from itertools import cycle, islice

s = input()
t = input()
u = "".join(islice(cycle(s), len(s)+len(t)))

print("Yes" if u.find(t) >= 0 else "No")