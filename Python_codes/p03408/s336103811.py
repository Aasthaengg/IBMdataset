N = int(input())
s = [input() for _ in range(N)]
M = int(input())
t = [input() for _ in range(M)]

s.sort()
S = []
S.append(s[0])
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        S.append(s[i+1])

MAX = 0
for i in S:
    d = s.count(i) - t.count(i)
    MAX = max(MAX, d)

print(MAX)
