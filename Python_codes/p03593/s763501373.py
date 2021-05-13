import collections

H, W  = map(int, input().split())
A = []
for _ in range(H):
    for c in input():
        A.append(c)
A.sort()
B = collections.Counter(A).most_common()
# print(A)
# print(B)
success = False
if H % 2 == 0 and W % 2 == 0:
    if all([val[1] % 4 == 0 for val in B]):
        success = True
elif H % 2 == 1 and W % 2 == 0:
    if all([val[1] % 2 == 0 for val in B]):
        four = 0
        two = 0
        for el in B:
            x = el[1]
            if x % 4 == 0:
                four += 1
            elif x % 2 == 0:
                two += 1
        if two <= W // 2 and (W // 2 - two) % 2 == 0:
            success = True
elif H % 2 == 0 and W % 2 == 1:
    if all([val[1] % 2 == 0 for val in B]):
        four = 0
        two = 0
        for el in B:
            x = el[1]
            if x % 4 == 0:
                four += 1
            elif x % 2 == 0:
                two += 1
        if two <= H // 2 and (H // 2 - two) % 2 == 0:
            success = True
else:
    odd = 0
    two = 0
    four = 0
    for el in B:
        x = el[1]
        if x % 2 == 1:
            odd += 1
            x -= 1
        if x % 4 == 0:
            four += 1
        elif x % 2 == 0:
            two += 1
    if odd == 1:
        if two <= H // 2 + W // 2 and (H // 2 + W // 2- two) % 2 == 0:
            success = True
if success:
    print('Yes')
else:
    print('No')