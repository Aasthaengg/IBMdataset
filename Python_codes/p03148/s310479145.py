def solve():
    from collections import deque, namedtuple
    from operator import attrgetter
    import sys

    input = sys.stdin.readline
    Sushi = namedtuple('Sushi', 'taste kind')

    n, k = map(int, input().split())

    e = []
    for _ in range(n):
        t, d = map(int, input().split())
        e.append(Sushi(taste=d, kind=t - 1))

    e.sort(key=attrgetter('taste'), reverse=True)

    ret = 0
    used = [False] * n  # 選択されている種類
    q = deque()  # 選択から外す候補,[high->low]
    x = 0  # 暫定選択の種類数
    for s in e[:k]:  # 美味しさ降順k個
        if used[s.kind]:
            q.append(s)  # 同じ種類の2個目以降のみ交換候補になる
        else:
            used[s.kind] = True
            x += 1
        ret += s.taste
    ret += pow(x, 2)  # 種類ボーナス

    t = ret
    r = iter(e[k:])  # 交換で入れる候補
    while q:
        rem = q.pop()  # 選択から外す
        t -= rem.taste
        for s in r:
            if used[s.kind]:
                continue
            used[s.kind] = True
            t += s.taste + x * 2 + 1
            x += 1
            ret = max(ret, t)
            break
        else:
            break

    return ret


if __name__ == '__main__':
    print(solve())

# k個持っておいて、下位を交換する
