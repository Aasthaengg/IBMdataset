import sys
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    sushi = []
    neta = set([])
    for _ in range(N):
        t, d = map(int, input().split())
        sushi.append((d, t))
        neta.add(t)
    sushi.sort()
    L = len(neta)

    eat_kind = set([])
    same_kind = []
    point = 0
    for _ in range(K):
        d, t = sushi.pop()
        point += d
        if t not in eat_kind:
            eat_kind.add(t)
        else:
            same_kind.append((d, t))
    l = len(eat_kind)
    point += l ** 2
    #print("l={}, point={}".format(l, point))

    """
    貪欲でおいしいもの順にネタを取った後、新しい種類のネタにどんどんスイッチしていく方針はあっていたのに
    実装がヘビーになりすぎるから考えを間違っているだろうと撤退したのが愚かだった...!
    
    今は実装力を上げるパートということですね。
    """

    remain = [(d, t) for d, t in sushi if t not in eat_kind]
    remain.sort()
    #print("remain={}".format(remain))
    val = point # 前状態のポイント
    for i in range(l, L): # 前よりポイントが下がったとしてもどんどんネタの入れ替えをしていく！
        val = val - i ** 2 + (i + 1) ** 2
        if not same_kind: break
        pre_d, _ = same_kind.pop()
        val -= pre_d
        if not remain: break
        d, t = remain.pop()
        while t in eat_kind: d, t = remain.pop()
        val += d
        eat_kind.add(t)
        point = max(point, val)
        #print("l={}, point={}".format(i, val))

    print(point)

    



if __name__ == "__main__":
    main()
