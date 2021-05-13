

N = int(input())
A = list(map(int, input().split()))



accum = [0] * N
accum[0] = A[0]
for i in range(1,N):
    accum[i] = accum[i-1] + A[i]


# +-+-+-+-
ans1 = 0
tmp = [0] * N
for i in range(N):
    if i == 0:
        tmp[i] = A[i]
    else:
        tmp[i] = tmp[i-1] + A[i]

    if i % 2 == 0:
        if tmp[i] <= 0:
            ans1 += abs(tmp[i]) + 1
            tmp[i] = 1
    else:
        if tmp[i] >= 0:
            ans1 += abs(tmp[i]) + 1
            tmp[i] = -1

# -+-+-+-+
ans2 = 0
tmp = [0] * N
for i in range(N):
    if i == 0:
        tmp[i] = A[i]
    else:
        tmp[i] = tmp[i-1] + A[i]

    if i % 2 == 1:
        if tmp[i] <= 0:
            ans2 += abs(tmp[i]) + 1
            tmp[i] = 1
    else:
        if tmp[i] >= 0:
            ans2 += abs(tmp[i]) + 1
            tmp[i] = -1

print(min(ans1,ans2))

