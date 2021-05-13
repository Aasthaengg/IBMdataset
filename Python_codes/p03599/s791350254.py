A, B, C, D, E, F = list(map(int, input().split()))

s1 = set()
for i in range(0, 31, A):
    for j in range(0, 31, B):
        if 0 < i + j and i * 100 + j * 100 <= F:
            s1.add(i + j)

s2 = set()
for i in range(0, F, C):
    for j in range(0, F, D):
        if i + j <= F:
            s2.add(i + j)

concent = 0
total = 0
sugar = 0
for ab in s1:
    for cd in s2:
        if cd / ab <= E and ab * 100 + cd <= F:
            if concent <= cd / ab:
                concent = cd / ab
                total = ab * 100 + cd
                sugar = cd


print(total, sugar)
