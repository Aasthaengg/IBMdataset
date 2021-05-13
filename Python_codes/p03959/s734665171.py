N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7
if N == 1:
    if T[0] == A[0]:
        print(1)
    else:
        print(0)
    exit()

ans = 1
for i in range(1, N - 1):
    if T[i] == T[i - 1] and A[i] == A[i + 1]:
        ans *= min(T[i], A[i])
        ans %= MOD
    elif T[i] > T[i - 1] and A[i] == A[i + 1] and A[i] < T[i]:
        print(0)
        exit()
    elif T[i] == T[i - 1] and A[i] > A[i + 1] and A[i] > T[i]:
        print(0)
        exit()
    elif T[i] > T[i - 1] and A[i] > A[i + 1] and A[i] != T[i]:
        print(0)
        exit()
print(ans)

