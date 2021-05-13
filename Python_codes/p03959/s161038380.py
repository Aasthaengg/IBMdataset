# CODE FESTIVAL 2016 qual C C - 二人のアルピニスト / Two Alpinists
N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
T = [0] + T + [T[-1]]
A = [A[0]] + A + [0]

K = [0 for k in range(N+2)]
L = [0 for k in range(N+2)]
for k in range(1,N+2):
    if T[k-1] != T[k]:
        K[k] = T[k]
for k in range(1,N+2):
    if A[N-k+2] != A[N-k+1]:
        L[N-k+1] = A[N-k+1]

MOD = 10**9 + 7
ans = 1
for k in range(1,N+1):
    if K[k] == L[k] == 0:
        ans *= min(A[k],T[k])
        ans %= MOD
    elif (K[k]>0 and A[k]<K[k]) or (L[k]>0 and T[k]<L[k]):
        print(0)
        exit(0)
print(ans)
