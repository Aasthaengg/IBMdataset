from collections import Counter

n=int(input())

def soinsu(n):
    S = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            S.append(i)
    if S == []:
        S.append(n)
    else:
        if n != 1:
            S.append(n)
    return S
L=[]
if n >= 2:
    for i in range(2, n + 1):
        L = L + soinsu(i)
LC = Counter(L)

C2 = 0
C4 = 0
C14 = 0
C24 = 0
C74 = 0

for v in LC.values():
    if v >= 2:
        C2 += 1
        if v >= 4:
            C4 += 1
            if v >= 14:
                C14 += 1
                if v >= 24:
                    C24 += 1
                    if v >= 74:
                        C74 += 1

r = C4 * (C4 - 1) // 2 * (C2 - 2) + C14 * (C4 - 1) + C24 * (C2 - 1) + C74

print(r)