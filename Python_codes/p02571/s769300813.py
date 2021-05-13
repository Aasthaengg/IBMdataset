S = input()
T = input()

s = len(S)
t = len(T)

ans = 1e10

for i in range(s - t + 1):
    a = 0
    for j in range(t):
        if S[i+j] != T[j]:
            a += 1
    ans = min(a, ans)

print(ans)