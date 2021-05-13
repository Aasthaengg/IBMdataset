n, m = map(int, input().split(" "))
a = map(int, input().split(" "))

mods = {}
mods[0] = 1
sum = 0
ans = 0
for i in a:
    sum += i
    mod = sum % m
    # print("sum/mod  %d/%d" % (sum, mod))

    if mod in mods.keys():
        mods[mod] = mods[mod] + 1
    else:
        mods[mod] = 1

for mod, count in mods.items():
    # print("mod,count = %d,%d" % (mod, count))
    if count < 2:
        continue
    else:
        ans += (count * (count - 1) / 2)

print(int(ans))
