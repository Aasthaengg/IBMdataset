K = int(input())
A = list(map(int, input().split()))

lo = 2
hi = 10**18


def check1(people):
    for a in A:
        people = (people // a) * a
    if people > 2:
        return False
    else:
        return True


def check2(people):
    for a in A:
        people = (people // a) * a
    if people < 2:
        return False
    else:
        return True


for i in range(100):
    center = (lo + hi) // 2
    if check1(center):
        lo = center
    else:
        hi = center

Mz = center

lo = 2
hi = 10**18

for i in range(100):
    center = (lo + hi) // 2
    if center > Mz:
        hi = center
        continue
    if check2(center):
        hi = center
    else:
        lo = center

mz = hi
if Mz >= mz:
    print(mz, Mz)
else:
    print(-1)