from bisect import bisect_right
s = input()
t = input()
n = len(s)

position = [[] for i in range(26)]
for i, ss in enumerate(s):
    pos = ord(ss)-ord("a")
    position[pos].append(i)

for tt in set(t):
    if not position[ord(tt)-ord("a")]:
        print(-1)
        exit(0)

count = 0
idx = -1
for tt in t:
    t_i = ord(tt)-ord("a")
    pos = bisect_right(position[t_i], idx)
    if pos == len(position[t_i]):
        idx = position[t_i][0]
        count += 1
    else:
        idx = position[t_i][pos]

print(count*n+idx+1)
