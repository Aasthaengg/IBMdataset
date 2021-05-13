'''
        2 A1 = M_1 + M_2
        2 A2 = M_2 + M_3
        2 A3 = M_3 + M_4
        2 A4 = M_4 + M_5
        2 A5 = M_5 + M_1
A1 + A2 + A3 = M_1 + M_2 + M_3

M_1 = (A1 + A2 + A3) - (M_2 + M_3 + M_4 + M_5)
M_2 = (A1 + A2 + A3) - (M_3 + M_4 + M_5 + M_6)
M_3 = (A1 + A2 + A3) - (M_4 + M_5 + M_6 + M_7)
'''

n    = int(input())
ai   = list(map(int, input().split()))
aix2 = list(map(lambda x: x * 2, ai))

sum_a = sum(ai)

def ring_get(xs, s, e, mod):
    ys = []
    i  = s % mod

    while i != (e % mod):
        ys.append(xs[i])
        i = (i + 2) % mod

    return ys

beforeM = sum_a - sum(ring_get(aix2, 1, 1 + (n - 1), n))

print(beforeM)

for i in range(1, n):
    print(aix2[i - 1] - beforeM)
    beforeM = aix2[i - 1] - beforeM
