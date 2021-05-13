import copy
S = list(map(str, input().rstrip()))

vari = set(S)

ans = float("inf")

for v in vari:
    s = copy.deepcopy(S)
    while len(s) != s.count(v):
        for i in range(1, len(s)):
            if s[i] == v:
                s[i - 1] = v
        s = s[:-1]
    ans = min(ans, len(S) - len(s))

print(ans)