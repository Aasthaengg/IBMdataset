n = int(input())
T = tuple(map(int, input().split()))
A = tuple(map(int, input().split()))
mod = 10**9+7

mt = T[-1]
ma = A[0]
if mt != ma:
    print(0)
else:
    ans = 1
    for i in range(1, n-1):
        if T[i-1] == T[i] and A[i] == A[i+1]:
            ans *= min(T[i], A[i])
            ans %= mod
        if T[i] == A[i] and (T[i] != mt or A[i] != ma):
            print(0)
            break
        if ((T[i] > T[i-1] and T[i] > A[i]) or
            (A[i] > A[i+1] and T[i] < A[i])):
            print(0)
            break
    else:
        print(ans)
