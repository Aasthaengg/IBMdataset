n = int(input())
F = [list(map(int,input().split())) for _ in range(n)]
P = [list(map(int,input().split())) for _ in range(n)]
ans = -1e100
for i in range(1,2**10):
    A = [0]*10
    profit = 0
    j = 0
    while i > 0:
        A[j] += i&1
        j += 1
        i = i >> 1
    for j in range(n):
        dup = 0
        for a,f in zip(A,F[j]):
            dup += a&f
        profit += P[j][dup]
    ans = max(ans,profit)
print(ans)
