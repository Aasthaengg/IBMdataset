N = int(input())
A = list(map(int, input().split()))
B = []
C = []

B_append = B.append
C_append = C.append
#0をひとまとめにする
count = 0
for a in A:
    if a != 0:
        if count != 0:
            B_append(0)
            C_append(count)
        B_append(a)
        C_append(1)
        count = 0
    else:
        count += 1
if count != 0:
    B_append(0)
    C_append(count)

# print (A)
# print (B)
# print (C)
N = len(B)

count = 0
for l in range(N):
    tmp = C[l] #スタート地点の数
    tmp_count = 0
    total = B[l]
    xor = B[l]
    for r in range(l + 1, N): #せいぜい20 * 2 (0と1ビット立つのが繰り返された時)
        total += B[r]
        xor ^= B[r]
        if total == xor:
            tmp_count += C[r]
        else:
            break #条件を満たさなくなった時ループから抜ける
    count += tmp_count * tmp
    count += (tmp * (tmp + 1)) // 2

print (count)