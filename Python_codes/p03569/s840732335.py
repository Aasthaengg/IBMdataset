s = input()

core = []

for c in s:
    if c != 'x':
        core.append(c)
if core == []:
    print(0)
    exit()
l = 0
r = len(core) - 1

while l <= r:
    if core[l] != core[r]:
        print(-1)
        exit()
    l += 1
    r -= 1

ans = 0
l = 0
r = len(s) - 1

while l <= r:
    lx = 0
    rx = 0
    while s[l] == 'x':
        l += 1
        lx += 1
    while s[r] == 'x':
        r -= 1
        rx += 1
    ans += abs(lx - rx)
    l += 1
    r -= 1
print(ans)
