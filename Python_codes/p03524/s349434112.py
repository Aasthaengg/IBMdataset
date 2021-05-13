s = input()

a, b, c = 0, 0, 0

for i in range(len(s)):
    if s[i] == "a":
        a += 1
    elif s[i] == "b":
        b += 1
    else:
        c += 1


def func(j, k):
    if j + 1 == k or j - 1 == k or j == k:
        return True
    else:
        return False

ab, bc, cd = False, False, False
ab = func(a, b)
bc = func(b, c)
ca = func(c, a)

if ab and bc and ca:
    print("YES")
else:
    print("NO")