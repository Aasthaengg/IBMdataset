N = int(input())
S = input()
T = input()
ans = 3 if S[0] == T[0] else 6
for i in range(1, N):
    if S[i-1] == T[i-1]:
        ans *= 2
    elif S[i] == S[i-1]:
        pass
    else:
        ans *= 1 if S[i] == T[i] else 3
print(ans % (10**9+7))