import bisect

s = list(input())
t = list(input())

if not set(t).issubset(set(s)):
    print(-1)
    exit()

indices = [[] for _ in range(26)]
idx = [0]*26

for i in range(len(s)):
    indices[ord(s[i]) - 97].append(i)

now = 0
rep = 1
for i in range(len(t)):
    x = ord(t[i]) - 97
    y = bisect.bisect_left(indices[x], now)
    if y == len(indices[x]):
        rep += 1
        now = indices[x][0] + 1
    else:
        now = indices[x][y] + 1

print(len(s)*(rep-1) + now)