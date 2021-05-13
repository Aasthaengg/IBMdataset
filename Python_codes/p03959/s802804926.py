N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
if T[-1] != A[0] or T.index(T[-1]) > N - 1 - A[::-1].index(A[0]):
    print(0)
    exit()
ans = 1
MOD = 10 ** 9 + 7
for i in range(1, N - 1):
    t_comb = 1
    if T[i - 1] == T[i]:
        t_comb *= T[i]

    a_comb = 1
    if A[i] == A[i + 1]:
        a_comb *= A[i]
    ans = (ans * min(t_comb, a_comb)) % MOD
print(ans)