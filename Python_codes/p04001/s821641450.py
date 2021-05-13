ss = input()
ans = []

def bfs(exp, x):
    # 探索終了
    if x == len(ss):
        return exp
    nxt = None
    # まだ使っていない数字を求める
    if exp[-1] == '+':
        nxt = ss[x]
        ret = bfs(exp+nxt, x+1)
        if ret:
            s_ = sum([int(i) for i in ret.split("+")])
            ans.append(s_)
    else:
        nxt = ss[x]
        ret = bfs(exp+nxt, x+1)
        if ret:
            s_ = sum([int(i) for i in ret.split("+")])
            ans.append(s_)
        ret = bfs(exp+'+', x)
        if ret:
            s_ = sum([int(i) for i in ret.split("+")])
            ans.append(s_)
if len(ss) == 1:
    print(int(ss))
else:
    bfs(ss[0],1)
    print(sum(ans))