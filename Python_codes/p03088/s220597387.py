import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(input())
    chars = "ACGT"

    if n == 3:
        print(61)
        sys.exit()
    elif n == 4:
        print(230)
        sys.exit()

    from collections import deque, Counter
    que = deque()

    for ch1 in chars:
        for ch2 in chars:
            que.append((ch1 + ch2, 2))

    ans = 0
    str_set = set()
    counter = Counter()

    while que:
        cur, length = que.popleft()
        length_next = length + 1
        for ch in chars:
            ok = True
            nx = cur + ch
            if length_next == 3:
                if "AGC" in nx:
                    continue
                for j in range(2):
                    sl = list(nx)
                    sl[j], sl[j + 1] = sl[j + 1], sl[j]
                    swap = "".join(sl)
                    if "AGC" in swap:
                        ok = False
                if ok:
                    que.append((nx, length_next))
            if length_next == 4:
                if "AGC" in nx:
                    ok = False
                for j in range(3):
                    sl = list(nx)
                    sl[j], sl[j + 1] = sl[j + 1], sl[j]
                    swap = "".join(sl)
                    if "AGC" in swap:
                        ok = False
                if ok:
                    counter[nx] += 1
                    str_set.add(nx)

    for _ in range(n - 4):
        counter_next = Counter()
        for st in str_set:
            for ch in chars:
                nx = st[1:] + ch
                if nx in str_set:
                    counter_next[nx] += counter[st]
                    counter_next[nx] %= MOD
        counter = counter_next

    ans = sum(counter.values())
    ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
