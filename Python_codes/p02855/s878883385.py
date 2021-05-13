h, w, k = map(int, input().split())
ans = []
num = 0
for _ in range(h):
    s_ = input()
    s_ = [i for i in range(w) if s_[i] == "#"]
    if not s_:
        ans.append([])
        continue
    l = [0]*w
    for i in s_:
        num += 1
        l[i] = num
    n_ = 0
    for wi in range(w):
        if l[wi] == 0:
            l[wi] = n_
        else:
            n_ = l[wi]
    if s_[0] != 0:
        l[:s_[0]] = [l[s_[0]]]*s_[0]
    ans.append(l)
l = []
for hi in range(h):
    if not ans[hi]:
        if not l: continue
        ans[hi] = l
    elif ans[hi]:
        l = ans[hi].copy()
l = []
for hi in reversed(range(h)):
    if not ans[hi]:
        if not l: continue
        ans[hi] = l
    elif ans[hi]:
        l = ans[hi].copy()
for i in range(h): print(*ans[i])