M, K = map(int, input().split())
m = 1 << M

if K >= m:
    print(-1)
    exit()

if M == 0:
    print(0, 0)
    exit()

if M == 1:
    if K == 0:
        print(0, 0, 1, 1)
    else:
        print(-1)
    exit()

k = str(K)
seq = list(map(str, range(m)))
seq.remove(k)
answer = seq + [k] + seq[::-1] + [k]

print(' '.join(answer))
