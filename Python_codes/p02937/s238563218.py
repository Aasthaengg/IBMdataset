import bisect

s = input()
t = input()

d = dict()

for i, ch in enumerate(s):
    if ch in d:
        d[ch].append(i)
    else:
        d[ch] = [i]

ret = 0
cindex = -1

for ch in t:
    if ch not in d:
        print(-1)
        exit()
    else:
        ls = d[ch]
        index = bisect.bisect_right(ls, cindex)
        index = 0 if (index == len(ls)) else index
        if cindex < ls[index]:
            ret += (ls[index] - cindex)
            cindex = ls[index]
        else:
            ret += len(s) + ls[index] - cindex
            cindex = ls[index]

print(ret)
