from bisect import bisect_left
import sys
s = input()
t = input()

d = {char:[] for char in 'abcdefghijklmnopqrstuvwxyz'}
for i in range(len(s)):
    d[s[i]].append(i)

cnt = 0
index = 0
for char in t:
    if not d[char]:
        print(-1)
        sys.exit()
    i = bisect_left(d[char], index)
    if i == len(d[char]):
        cnt += 1
        index = d[char][0]
    else:
        index = d[char][i]
    index += 1

ans = cnt * len(s) + index
print(ans)