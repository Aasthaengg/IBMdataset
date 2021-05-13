# ABC117D

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for d in range(40, -2, -1):
    if d != -1 and not (K & 1 << d):
        continue
    
    tmp = 0
    for e in range(40, -1, -1):
        mask = 1 << e
        num_1 = 0
        for i in range(N):
            if A[i] & mask:
                num_1 += 1
        if e > d:
            if K & mask:
                tmp += mask * (N - num_1)
            else:
                tmp += mask * num_1
        elif e == d:
            tmp += mask * num_1
        else:
            tmp += mask * max(num_1, N - num_1)
    
    ans = max(ans, tmp)

print(ans)