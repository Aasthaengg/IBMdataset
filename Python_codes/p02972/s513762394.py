N = int(input())
A = [0] + list(map(int, input().split()))

B = [0] * (N + 1)

for i in range(N, 0, -1):
    # mod2 の足し算は xor
    sum_a = 0
    for j in range(i + i, N + 1, i):
        sum_a ^= B[j]
    B[i] = sum_a ^ A[i]

# print(A, B)
out = []
for i in range(1, N + 1):
    if B[i] == 1:
        out.append(i)
if len(out) > 0:
    print(len(out))
    print(*out)
else:
    print(0)
