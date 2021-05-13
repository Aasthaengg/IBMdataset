from collections import Counter

H, W = map(int, input().split())

num = [0]*5

for h in range(-(-H//2)):
    for w in range(-(-W//2)):
        tmp = 1
        if h < H//2:
            tmp *= 2
        if w < W//2:
            tmp *= 2
        num[tmp] += 1

s = ""
for _ in range(H):
    s += input()

c = list(Counter(s).values())
c.sort(reverse = True)

four = 0
for i in range(len(c)):
    if four == num[4]:
        break
    while c[i] >= 4:
        c[i] -= 4
        four += 1
        if four == num[4]:
            break

two = 0
for i in range(len(c)):
    if two == num[2]:
        break
    while c[i] >= 2:
        c[i] -= 2
        two += 1
        if two == num[2]:
            break

print("Yes" if sum(c) == num[1] and four == num[4] and two == num[2] else "No")