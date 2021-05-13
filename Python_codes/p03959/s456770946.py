MOD = 1000000007

N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))

H0 = [None for _ in range(N)]
H1 = [None for _ in range(N)]

incorrect = False

maxh = 0
for i in range(N):
    if maxh < T[i]:
        H0[i] = T[i]
        maxh = T[i]

maxh = 0
for i in reversed(range(N)):
    if H0[i] != None and H0[i] > A[i]:
        incorrect = True
    if maxh < A[i]:
        H1[i] = A[i]
        maxh = A[i]

ans = 1
for i in range(N):
    if H0[i]==None and H1[i]==None:
        ans *= min(A[i],T[i])
        ans %= MOD

print(ans if not incorrect else 0)