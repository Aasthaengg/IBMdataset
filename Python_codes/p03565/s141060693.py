S = input()
T = input()
s, t = len(S), len(T)
c = "z" * s
for i in range(s - t + 1):
    if all(S[i + j] in (T[j], "?") for j in range(t)):
        c = min(c, S[:i] + T + S[i + t:])
print("UNRESTORABLE" if c == "z" * s else c.replace("?", "a"))
