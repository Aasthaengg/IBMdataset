import sys

input = sys.stdin.readline

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

if N == 1:
    if T[0] == A[0]:
        print(1)
    else:
        print(0)
    sys.exit()

mod = 10**9 + 7
ans = 1
for i in range(N):
    if i == 0:
        if A[i] < T[i]:
            print(0)
            sys.exit()
    elif i == N-1:
        if T[i] < A[i]:
            print(0)
            sys.exit()
    else:
        if T[i-1] < T[i] and A[i+1] < A[i] and T[i] != A[i]:
            print(0)
            sys.exit()
        else:
            if T[i-1] < T[i]:
                if A[i] < T[i]:
                    print(0)
                    sys.exit()
            elif A[i+1] < A[i]:
                if T[i] < A[i]:
                    print(0)
                    sys.exit()
            else:
                ans *= min(T[i], A[i])
                ans %= mod

print(ans)