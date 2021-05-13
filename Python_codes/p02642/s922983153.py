N = int(input())
M = 10 ** 6
A = list(map(int, input().split()))
B = [0] * (M + 1)
for a in A:
    B[a] +=1
C = [1] * (M + 1)
A = set(A)
for i in A:
    for j in range(i, M + 1, i):
        if i == j:
            if B[i] > 1:
                C[i] = 0
        else:
            C[j] = 0
ans = 0
for a in A:
    if C[a]:
        ans += 1
print(ans)
