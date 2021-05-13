t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
atot1 = (a1 - b1) * t1
atot2 = (a2 - b2) * t2
if atot1 > 0:
    atot1 *= -1
    atot2 *= -1


if atot1 + atot2 < 0:
    print(0)
    exit()
if atot1 == - atot2:
    print('infinity')
    exit()
S = (-atot1) // (atot1 + atot2)
T = (-atot1) % (atot1 + atot2)
if T != 0:
    print(2 * S + 1)
else:
    print(2 * S)
