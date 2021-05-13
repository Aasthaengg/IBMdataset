N, M = map(int, input().split())
ac = [0]*N
wa = 0

for i in range(M):
    P, S = map(str, input().split())
    P = int(P)-1
    if ac[P] != 1 and S == "AC":
        wa += abs(ac[P])
        ac[P] = 1
    elif ac[P] != 1 and S == "WA":
        ac[P] -= 1

print(ac.count(1), wa)
