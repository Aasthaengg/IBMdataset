S = input()
cand = set()
for i in range(2 ** 4):
    target = list("AKIHABARA".replace("A", "*"))
    if i & (1 << 0):
        target[0] = "A"
    if i & (1 << 1):
        target[4] = "A"
    if i & (1 << 2):
        target[-3] = "A"
    if i & (1 << 3):
        target[-1] = "A"
    t = "".join(target)
    t = t.replace("*", "")
    cand.add(t)
if S in cand:
    print("YES")
else:
    print("NO")
