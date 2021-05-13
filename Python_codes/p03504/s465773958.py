import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    pn, cn = map(int, input().split())
    st = [[set(), set()] for _ in range(cn)]
    # 同じチャンネルの連続した番組を結合
    for _ in range(pn):
        s, t, c = map(int, input().split())
        c -= 1
        if s in st[c][1]:
            st[c][1].remove(s)
            if t in st[c][0]:
                st[c][0].remove(t)
            else:
                st[c][1].add(t)
        elif t in st[c][0]:
            st[c][0].remove(t)
            st[c][0].add(s)
        else:
            st[c][0].add(s)
            st[c][1].add(t)
    #print(st)
    # 座標圧縮
    tt = set()
    for c_st in st:
        for s in c_st[0]:
            tt.add(s)
        for t in c_st[1]:
            tt.add(t)
    tn = len(tt)
    ttoi = {}
    for i, t in enumerate(sorted(tt)):
        ttoi[t] = i
    #print(ttoi)
    # imos法のためにチャンネル数の増減をcntに入力
    cnt = [0] * (tn + 1)
    for c_st in st:
        for s in c_st[0]:
            i = ttoi[s]
            cnt[i] += 1
        for t in c_st[1]:
            i = ttoi[t]
            cnt[i + 1] -= 1
    #print(cnt)
    # 累積和をとって最大のチャンネル数を取得
    ans = 0
    for i in range(tn):
        cnt[i + 1] += cnt[i]
        ans = max(ans, cnt[i + 1])
    #print(cnt)
    print(ans)

main()
