import bisect

S = input().strip()
T = input().strip()

x = [[] for j in range(26)]

for i, s in enumerate(S):
    x[ord(s) - ord('a')].append(i)

sett = list(set(T))

for t in sett:
    if len(x[ord(t) - ord('a')]) == 0:
        print(-1)
        exit()

c = 0
z = 0

for t in T:
    y = bisect.bisect_left(x[ord(t) - ord('a')], c)
    if y == len(x[ord(t) - ord('a')]):
        z += 1
        c = x[ord(t) - ord('a')][0] + 1
    else:
        c = x[ord(t) - ord('a')][y] + 1

print(z * len(S) + c)
