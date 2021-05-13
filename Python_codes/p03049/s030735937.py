import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def diverta19_c():
    _ = int(readline())
    S = [ln.strip().decode('UTF-8') for ln in read().split()]

    # _AB_ , B_A , B_ , _A の個数をそれぞれ数える
    inner, st, ed, sted = 0, 0, 0, 0
    for si in S:
        inner += si.count('AB')
        if si[0] == 'B' and si[-1] == 'A': sted += 1
        elif si[0] == 'B': st += 1
        elif si[-1] == 'A': ed += 1

    ans = inner  # これは確定
    if sted > 0:
        ans += (sted - 1)  # x個でx-1組のABができる
        if st > 0:
            ans += 1  # B_A + B_ で1組
            st -= 1
        if ed > 0:
            ans += 1  # _A + B_A で1組
            ed -= 1
    ans += min(st, ed)  # _A + B_ で1組
    print(ans)

diverta19_c()