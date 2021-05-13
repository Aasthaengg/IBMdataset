S = input()
T = input()
ans = [0] * (len(S) - len(T)+1)
for a in range(len(S) - len(T)+1):
    for b in range(len(T)):
        if S[a + b] != T[b]:
            ans[a] += 1

print(min(ans))
