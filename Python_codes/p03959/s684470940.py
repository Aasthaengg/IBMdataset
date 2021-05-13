import sys


def LI():
    return list(map(int, input().split()))


mod = pow(10, 9)+7
N = int(input())
T = LI()
A = LI()
ans = 1
if N == 1:
    if T == A:
        print(1)
    else:
        print(0)
    sys.exit()
if N == 2:
    if T[1] == A[0]:
        print(1)
    else:
        print(0)
if T[N-1] != A[0]:
    print(0)
    sys.exit()
for i in range(1, N-1):
    if T[i-1] != T[i]:
        if A[i] < T[i]:
            print(0)
            sys.exit()
        continue
    if A[i] != A[i+1]:
        if A[i] > T[i]:
            print(0)
            sys.exit()
        continue
    ans = (ans * min(T[i], A[i])) % mod
print(ans)
