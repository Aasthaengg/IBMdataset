N = int(input())
S1 = input().strip()
S2 = input().strip()

ans = 1

T = [0] * len(S1)

if S1[0] == S2[0]:
    T[0] = 1
else:
    T[0] = T[1] = 1
    ans *= 2

ans *= 3
MOD = 10 ** 9 + 7

for i in range(len(S1)-1):
    if T[i] == 0:
        T[i] = 1
        if S1[i] == S1[i+1]:  # 2 or 4
            T[i+1] = 1
            if S1[i-1] == S2[i-1]:  # 2
                ans *= 2
                ans %= MOD
            else:  # 4
                ans *= 3
                ans %= MOD

        else:  # 1 or 3
            if S1[i-1] == S2[i-1]:  # 1
                ans *= 2
                ans %= MOD
            else:  # 3
                pass

if T[-1] == 0:
    if S1[-2] == S2[-2]:
        ans *= 2
        ans %= MOD

print(ans)
