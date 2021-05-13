N = int(input())
A = list(map(int, input().split()))
B = []
C = []

count = 0
for a in A:
    if a != 0:
        if count != 0:
            B.append(0)
            C.append(count)
        B.append(a)
        C.append(1)
        count = 0
    else:
        count += 1
if count != 0:
    B.append(0)
    C.append(count)

# print (A)
# print (B)
# print (C)
N = len(B)

count = 0
for l in range(N - 1):
    tmp = C[l] #スタート地点の数
    tmp_count = 0
    total = B[l]
    xor = B[l]
    for r in range(l + 1, N):
        total += B[r]
        xor ^= B[r]
        if total == xor:
            tmp_count += C[r]
        else:
            break
    # print (tmp_count, tmp)
    count += tmp_count * tmp
    count += (tmp * (tmp + 1)) // 2
    # print (count)

count += (C[-1] * (C[-1] + 1)) // 2

print (count)

