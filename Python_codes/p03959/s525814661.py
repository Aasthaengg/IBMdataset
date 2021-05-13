N = int(input())
Ts = list(map(int, input().split()))
As = list(map(int, input().split()))

maxs = [0] * N
musts = [None] * N
prev = 0
for i in range(N):
    t = Ts[i]
    if prev < t:
        musts[i] = t
    maxs[i] = t
    prev = t

prev = 0
for i in range(N-1, -1, -1):
    a = As[i]
    if prev < a:
        if (musts[i] and musts[i] != a) or maxs[i] < a:
            print(0)
            exit()
        musts[i] = a
    maxs[i] = maxs[i] if maxs[i] < a else a
    prev = a

ans = 1
MOD = 10 ** 9 + 7
for i in range(N):
    if musts[i] is None:
        ans *= maxs[i]
        ans %= MOD
print(ans)
