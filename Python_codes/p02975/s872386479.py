from collections import Counter
N = int(input())
A = list(map(int, input().split()))

if sum(A) == 0:
    print('Yes')
    exit()

if len(A) % 3 != 0:
    print('No')
    exit()

c = Counter(A)
if len(c.values()) == 2:
    values = list(c.values())
    if min(values) == N // 3:
        keys = list(c.keys())
        if 0 in keys:
            print('Yes')
            exit()

if len(c.values()) != 3:
    print('No')
    exit()

keys = list(c.keys())
for i, j, k in ([0, 1, 2], [1, 2, 0], [2, 1, 0]):
    if keys[i] ^ keys[j] != keys[k]:
        print('No')
        exit()

values = list(c.values())
if values[0] != values[1] or values[1] != values[2]:
    print('No')
    exit()

print('Yes')

# a b c a b c ...
# a xor b = c
# b xor c = a
# c xor a = b

# 全員0

# x 0 x x 0 x ...
