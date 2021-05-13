S = input()

s_ = S[0]

ans = 0
for s in S[1:]:
    if s != s_:
        ans += 1
    s_ = s

print(ans)