M = 10 ** 9 + 7
S = input()
A = 0
AB = 0
ABC = 0
X = 1
for c in S:
    if c == 'C':
        ABC = (ABC + AB) % M
    elif c == 'B':
        AB = (AB + A) % M
    elif c == 'A':
        A = (A + X) % M
    elif c == '?':
        ABC = (3 * ABC + AB) % M
        AB = (3 * AB + A) % M
        A = (3 * A + X) % M
        X = (3 * X) % M
print(ABC)