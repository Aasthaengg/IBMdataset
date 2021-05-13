S = input()

ans = 0
l = 0

for c in S:
    l += 1
    if not c in ('A', 'C', 'G', 'T'):
        l = 0
    ans = max(ans, l)

print(ans)