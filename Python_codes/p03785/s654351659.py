N, C, K = map(int, input().split())
T = sorted([int(input()) for i in range(N)])
b = 0
i = 0
n = 1
t = T[0]
while i < N - 1:
    if n == C:
        b += 1
        n = 1
        i += 1
        t = T[i]
        if i == N - 1:
            b += 1
            break
        else:
            continue
    if t + K < T[i + 1]:
        b += 1
        n = 1
        i += 1
        t = T[i]
        if i == N - 1:
            b += 1
            break
        else:
            continue
    n += 1
    i += 1
    if i == N - 1:
        b += 1
        break

print(b)