N = int(input())
T = [0] + list(map(int, input().split())) + [0]
A = [0] + list(map(int, input().split())) + [0]

MOD = 10 ** 9 + 7


def imp():
    print(0)
    exit()


ans = 1
for i in range(1, N + 1):
    if T[i - 1] < T[i]:
        if A[i] < T[i]:
            imp()
    elif A[i] > A[i + 1]:
        if T[i] < A[i]:
            imp()
    else:
        ans = (ans * min(T[i], A[i]) % MOD)
print(ans)
