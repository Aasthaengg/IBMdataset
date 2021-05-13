S = input()
T = input()

len_t = len(T)
for i in reversed(range(len(S)-len_t + 1)):
    for j, s in enumerate(S[i:i+len_t]):
        if s != T[j] and s != "?":
            break
        if j == len_t - 1:
            res = S[:i] + T + S[i + len_t:]
            res = res.replace("?", "a")
            print(res)
            exit()

print("UNRESTORABLE")