NO = "UNRESTORABLE"
S = input()
N = len(S)
T = input()
M = len(T)

candidates = []
for i in range(N - M + 1):
    if all(S[i + j] == "?" or S[i + j] == T[j] for j in range(M)):
        candidates.append((S[:i] + T + S[i + M :]).replace("?", "a"))
if candidates:
    candidates.sort()
    print(candidates[0])
else:
    print(NO)
