N = int(input())
T = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

if T[N-1] != A[0]:
    print(0)
    exit()

fix = [False for i in range(N)]
fix[0] = True
for i in range(1, N):
    if T[i] > T[i-1]:
        fix[i] = True

# print(fix)

if fix[N-1] is True and T[N-1] != A[N-1]:
    print(0)
    exit()
else:
    fix[N-1] = True
    T[N-1] = A[N-1]

for j in range(N-2, 0, -1):
    if A[j] > A[j+1]:
        if fix[j] is True and A[j] != T[j]:
            print(0)
            exit()
        else:
            fix[j] = True
            T[j] = A[j]
    elif fix[j] is True and T[j] > A[j]:
        print(0)
        exit()
    elif fix[j] is not True:
        T[j] = min(T[j], A[j])


MOD = 10**9 + 7
ans = 1
for i in range(N):
    if fix[i] is False:
        ans *= T[i]
        ans %= MOD
print(ans)
