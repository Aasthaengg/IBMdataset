# heapqの方針で上手くいかなかった
# 解説放送を見てimosにした

def main():
    from collections import namedtuple
    from heapq import heappop, heappush
    import sys
    input = sys.stdin.readline

    Prog = namedtuple('Prog', 'L R')
    Prog.__eq__ = lambda self, other: self.R == other.R
    Prog.__lt__ = lambda self, other: self.R < other.R

    N, C = map(int, input().split())
    ps = tuple([] for _ in range(30))
    for _ in range(N):
        l, r, ch = map(int, input().split())
        heappush(ps[ch - 1], Prog(l, r))

    imos = [0] * (10 ** 5 + 1)
    for ps_ch in ps:
        while ps_ch:
            l, r = heappop(ps_ch)
            while ps_ch and ps_ch[0].L == r:
                r = ps_ch[0].R
                heappop(ps_ch)
            else:
                imos[l - 1] += 1
                imos[r] -= 1

    for i in range(10 ** 5):
        imos[i + 1] += imos[i]

    print(max(imos))


if __name__ == '__main__':
    main()
