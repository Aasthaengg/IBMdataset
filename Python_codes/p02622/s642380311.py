
S = input()
T = input()

N = len(S)

S = [S[i:i+1] for i in range(len(S))]
T = [T[i:i+1] for i in range(len(T))]

ans = 0

for k in range(N):
    if S[k] != T[k]:
        ans += 1

print(ans) 