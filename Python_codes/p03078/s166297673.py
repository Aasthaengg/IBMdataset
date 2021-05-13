X, Y, Z, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))[::-1]

A_B = []
for a in A:
    for b in B:
        A_B.append(a + b)

A_B = sorted(A_B)[::-1][:K]

ans = []
for a_b in A_B:
    for c in C:
        ans.append(a_b + c)

for a in sorted(ans)[::-1][:K]:
    print(a)