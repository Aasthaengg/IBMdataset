N = int(input())
s = []
for _ in range(N):
    line = input()
    s.append(line)

M = int(input())
t = []
for _ in range(M):
    line = input()
    t.append(line)

words = set(s)
ans = 0

for w in words:
    tmp = 0
    for si in s:
        if w == si:
            tmp += 1
    for ti in t:
        if w == ti:
            tmp -= 1
    ans = max(ans, tmp)
print(ans)
