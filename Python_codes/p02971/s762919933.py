# C - Exception Handling
N = int(input())
A = list(int(input()) for _ in range(N))
A_sorted = list((sorted(A, reverse = True)))
A_sorted = A_sorted[0:2]

ans = []
for i in A:
    if i == A_sorted[0]:
        ans.append(A_sorted[1])
    else:
        ans.append(A_sorted[0])

for j in ans:
    print(j)