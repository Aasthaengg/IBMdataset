s = input()
n = len(s)
ans = 1000
for t in set(s):
    ans = min(ans, max([len(l) for l in s.split(t)]))
print(ans)