s = input()

ans = 1000
for c in set(s):
    ans = min(ans, max([len(si) for si in s.split(c)]))
print(ans)