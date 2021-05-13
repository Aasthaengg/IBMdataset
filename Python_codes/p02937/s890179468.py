import sys

def LS2(): return list(sys.stdin.readline().rstrip())

s = LS2()
t = LS2()

from collections import defaultdict

dict_s = defaultdict(list)

for i in range(len(s)):
    dict_s[s[i]].append(i)

d = {}
for a in dict_s.keys():
    d[a] = 0

r = 0
u = -1
for a in t:
    if len(dict_s[a]) == 0:
        print(-1)
        exit()
    else:
        left = -1
        right = len(dict_s[a])
        while left + 1 < right:
            mid = (left + right)//2
            if dict_s[a][mid] > u:
                right = mid
            else:
                left = mid
        if right == len(dict_s[a]):
            r += 1
            u = dict_s[a][0]
        else:
            u = dict_s[a][right]

print(len(s)*r+u+1)


