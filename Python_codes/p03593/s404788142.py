from collections import Counter
h, w, *s = open(0).read().split()
h = int(h)
w = int(w)
s = Counter(list(''.join(s)))

one = two = four = 0

for k in s:
    if s[k] % 4 == 0:
        four += 1
    elif s[k] % 2 == 0:
        two += 1
    else:
        one += 1
limit_one = 0
limit_two = 0


def ans():
    if two <= limit_two and one <= limit_one:
        print("Yes")
    else:
        print("No")


if h & 1 and w & 1:
    limit_two = h // 2 + w // 2
    limit_one = 1
    ans()
elif h & 1:
    limit_two = w // 2
    ans()
elif w & 1:
    limit_two = h // 2
    ans()
else:
    limit_two = 0
    ans()
