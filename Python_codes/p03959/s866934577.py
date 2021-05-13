MOD = 10**9+7
n = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
n_cases = [0]*n
n_cases[0] = n_cases[-1] = 1
height = [0]*n
if T[-1] != A[0]:
    print(0)
    exit()
height[0] = T[0]
height[-1] = A[-1]
for i, (t1, t2) in enumerate(zip(T, T[1:]), 1):
    if t1 != t2:
        n_cases[i] = 1
        height[i] = t2

for i, (a1, a2) in enumerate(zip(A[::-1], A[::-1][1:]), 2):
    if a1 != a2:
        n_cases[-i] = 1
        if height[-i] == a2 or (height[-i] == 0 and a2 <= T[-i]):
            continue
        print(0)
        exit()

for i, (t, a) in enumerate(zip(T, A)):
    if n_cases[i]:
        continue
    n_cases[i] = min(t, a)


ans = 1
for x in n_cases:
    ans *= x
    ans %= MOD
print(ans)