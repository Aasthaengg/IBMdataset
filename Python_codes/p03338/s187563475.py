N = int(input())
S = input()
m = 0
for i in range(1, N):
    S1, S2 = S[:i], S[i:]
    S1 = set(S1)
    S2 = set(S2)
    now = len(S1&S2)
    if m < now:
        m = now
print(m)