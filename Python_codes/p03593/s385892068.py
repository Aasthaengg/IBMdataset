h, w = map(int, input().split())


table = {}
for i in range(h):
    a = input()
    for c in a:
        if c not in table:
            table[c] = 1
        else:
            table[c] += 1

mod0 = []
mod1_3 = []
mod2 = []
for key, value in table.items():
    if value % 4 == 0:
        mod0.append(key)
    elif value % 4 == 2:
        mod2.append(key)
    else:
        mod1_3.append(key)


if w % 2 == 0 and h % 2 == 0:
    if len(mod1_3) > 0 or len(mod2) > 0:
        print("No")
    else:
        print("Yes")

elif w % 2 == 0 or h % 2 == 0:
    if h % 2 == 0:
        w, h = h, w

    if w // 2 < len(mod2):
        print("No")
    elif len(mod1_3) > 0:
        print("No")
    else:
        print("Yes")
else:
    if len(mod1_3) == 1 and len(mod2) <= h // 2 + w // 2:
        print("Yes")
    else:
        print("No")
