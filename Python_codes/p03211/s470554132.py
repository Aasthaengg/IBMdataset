S = input()
S_len = len(S)
ans = 1000
for i in range(S_len - 2):
    t = int(S[i:i + 3])
    t_abs = abs(t - 753)
    ans = min(ans, t_abs)
print(ans)
