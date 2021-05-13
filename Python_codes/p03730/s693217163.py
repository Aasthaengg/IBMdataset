a, b, c = [int(i) for i in input().split()]

mods = []

tmp = a

while True:
    mod = tmp % b
    if mod not in mods:
        mods.append(mod)
        tmp += a
    else:
        break

if c in mods:
    print("YES")
else:
    print("NO")
