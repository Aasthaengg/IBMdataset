import collections
w = input()

cc = collections.Counter(w)

cond = True
for c in cc:
    cond &= cc[c] % 2 == 0


print("Yes" if cond else "No")
