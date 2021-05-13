R, G, B, N_1 = map(int, input().split())
cnt = 0

for r in range(N_1//R + 1):
    N_2 = N_1
    N_2 -= r*R
    for g in range(N_2//G + 1):
        N_3 = N_2
        N_3 -= g*G

        if N_3%B == 0:
            cnt += 1

print(cnt)
