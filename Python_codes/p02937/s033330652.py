import bisect
s = input()
t = input()
n = len(s)
m = len(t)
indices = [[] for _ in range(26)]
for i in range(n):
    indices[ord(s[i]) - ord('a')].append(i)
for i in range(n):
    indices[ord(s[i]) - ord('a')].append(i + n)

ans = 0
p = 0
for i in range(m):
    c = ord(t[i]) - ord('a')
    if len(indices[c]) == 0:
        print(-1)
        exit()
    p = indices[c][bisect.bisect_left(indices[c], p)] + 1
    if p >= n:
        p -= n
        ans += n
ans += p
print(ans)