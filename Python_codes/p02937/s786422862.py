from bisect import bisect_left

s = input()
t = input()
idx = [[] for _ in range(26)]
for i in range(len(s)):
    c = ord(s[i]) - ord('a')
    idx[c].append(i)
count = 0
index = -1
for i in range(len(t)):
    c = ord(t[i]) - ord('a')
    if len(idx[c]) == 0:
        print(-1)
        exit()
    j = bisect_left(idx[c], index+1)
    if j == len(idx[c]):
        count += 1
        index = idx[c][0]
    else:
        index = idx[c][j]
print(count*len(s) + index + 1)

