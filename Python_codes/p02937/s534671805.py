import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
s = input()
t = input()

l = [chr(v) for v in range(ord("a"), ord("z")+1)]
d = {c:i for i,c in enumerate(l)}

def snx(s, target=None, reverse=False, loop=False):
    """文字列sの各要素について、cがiより→で最初に現れる位置n[i][c]
    loop=Trueのとき周回した先のインデックスまで求める
    """
    if target is None:
        target = [chr(v) for v in range(ord("a"), ord("z")+1)]
    d = {c:None for c in target}
    nx = [[None]*len(target) for _ in range(len(s))]
    if not reverse:
        i = len(s)-1
        for c in reversed(s):
            d[c] = i
            for j,t in enumerate(target):
                nx[i][j] = d[t]
            i -= 1
        if loop:
            for i in range(len(s)):
                for j in range(len(target)):
                    if nx[i][j] is None:
                        nx[i][j] = nx[0][j]
    else:
        i = 0
        for c in s:
            d[c] = i
            for j,t in enumerate(target):
                nx[i][j] = d[t]
            i += 1
        if loop:
            for i in range(len(s)):
                for j in range(len(target)):
                    if nx[i][j] is None:
                        nx[i][j] = nx[-1][j]
    return nx
nx = snx(s, loop=True)
c = -1
ans = 0
for i in range(len(t)):
    nc = nx[(c+1)%len(nx)][d[t[i]]]
    if nc is None:
        ans = -1
        break
    elif nc>c:
        ans += nc-c
    else:
        ans += nc+len(s)-c
    c = nc
print(ans)