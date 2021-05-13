n = int(input())
S = [input() for _ in range(n)]
ans = 0
c = {}

for s in S:
    s = "".join(sorted(s))
    if s not in c.keys():
        c[s] = 1
    else:
        ans += c[s]
        c[s] += 1


print(ans)