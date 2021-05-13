# CODE FESTIVAL 2017 予選 A: B – fLIP
N, M, K = [int(s) for s in input().split()]

canDo = 'No'

for n in range(0, N + 1):
    for m in range(0, M + 1):
        if n * (M - m) + m * (N - n) == K:
            canDo = 'Yes'
            break

print(canDo)    