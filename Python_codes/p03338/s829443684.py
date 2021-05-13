N = int(input())
S = list(input())

ans = 0

for i in range(1, N + 1):
    a = list(set(S[:i]))
    b = list(set(S[i:]))
    ans_ = sum([b.count(x) for x in a])
    # print(ans_)
    ans = max(ans, ans_)

print(ans)
