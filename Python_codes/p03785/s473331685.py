N,C,K = map(int,input().split())
T = [int(input()) for _ in range(N)]
T.sort()

bus = 0
pas = 0
l = 0
r = 0
while l < N:
    if r == N:
        if pas == 0:
            break
        else:
            bus += 1
            break
    elif T[l] + K >= T[r]:
        pas += 1
        r += 1
        if pas == C:
            bus += 1
            l = r
            pas = 0
    else:
        l = r
        bus += 1
        pas = 0
print(bus)