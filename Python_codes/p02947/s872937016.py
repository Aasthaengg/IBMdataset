n = int(input())
S = {}
ans = 0

for i in range(n):
    s = list(input())
    s.sort()
    s_s = ''.join(s)
    if s_s in S:
        ans += S[s_s]
        S[s_s] += 1
    else:
        S[s_s] = 1

print(ans)