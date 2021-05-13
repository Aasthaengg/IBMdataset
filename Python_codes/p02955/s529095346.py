N, K = map(int, input().split())
A = list(map(int, input().split()))


def divisor(N):
    from math import sqrt
    D = []
    for i in range(1, int(sqrt(N)) + 1):
        if N % i == 0:
          D.append(i)
          D.append(N // i)

    return list(set(D))

s = sum(A)
divisors = divisor(s)
divisors.sort(reverse=True)

pride = 0
tention = 0
TKM = []
for d in divisors:
    for i, a in enumerate(A):
        l = -(a % d)
        h = d - (a % d)
        TKM.append((h, l))

    hekinan = sorted(TKM, key=lambda shisho: abs(shisho[0]))
    if abs(hekinan[0][0]) <= abs(hekinan[-1][1]):
        pride += abs(hekinan[0][0])
        tention += hekinan[0][0]
        hekinan = hekinan[1:]
    else:
        pride += abs(hekinan[-1][1])
        tention += hekinan[-1][1]
        hekinan = hekinan[:-1]
    while len(hekinan) != 0:
        if tention >= 0:
            pride += abs(hekinan[-1][1])
            tention += hekinan[-1][1]
            hekinan = hekinan[:-1]
        else:
            pride += abs(hekinan[0][0])
            tention += hekinan[0][0]
            hekinan = hekinan[1:]

    if pride // 2 <= K:
        print(d)
        break
    pride = 0
    tention = 0
    TKM = []

