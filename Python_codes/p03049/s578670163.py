N = int(input())
S = []
g1 = []
g2 = []
g3 = []

ans = 0
for _ in range(N):
    s = input()
    ans += s.count("AB")
    if s[0] == 'B' and s[-1] == 'A':
        g1.append(s)
    if s[0] == 'B' and s[-1] != 'A':
        g2.append(s)
    if s[0] != 'B' and s[-1] == 'A':
        g3.append(s)


# g1が存在しない = B* と *A の組を作る
if len(g1) == 0:
    ans += min(len(g2), len(g3))
    print(ans)

# B*A が存在する場合
else:
    if len(g2) + len(g3) == 0:
        # B*A しか存在しない場合，これをくっつける
        ans += len(g1) - 1
    else:
        # B*A がlen(g1)個
        # B*  がlen(g2)個
        # *A  がlen(g3)個 ある
        # -> *A B*A B* の形を作れるだけ作る
        ans += len(g1) + min(len(g2), len(g3))
        pass
    print(ans)
