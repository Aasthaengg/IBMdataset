Ss = input().rstrip()
Ts = input().rstrip()

ans = 0
for S, T in zip(Ss, Ts):
    ans += S == T

print(ans)
