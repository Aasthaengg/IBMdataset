import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

h,w,K = na()
s = []
for i in range(h):
    s.append(list(ns()))

ans = []
k = 1
bb = 0

for i in range(h):
    if '#' in s[i]:
        ret = []
        flag = True
        for j in range(w):
            if s[i][j] == '#':
                if flag:
                    flag = False
                else:
                    k+=1
            ret.append(k)
        ans.append(ret)
        k+=1
        if bb:
            for _ in range(bb):
                ans.append(ans[-1])
            bb = 0
    else:
        if len(ans) == 0:
            bb += 1
            continue
        ans.append(ans[-1])


for i in ans:
    print(*i,sep=' ')