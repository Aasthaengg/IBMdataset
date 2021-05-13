def solve() -> 'max(averages), count(max(averages))':
    from collections import Counter
    from functools import lru_cache
    n, a, b = map(int, input().split())
    v = tuple(sorted(map(int, input().split()), reverse=True))

    def max_ave_x() -> 'max(average),{counts_to_make_max_average}':
        ret = -1
        t = 0
        max_i = set()
        for i, e in enumerate(v, 1):
            t += e
            if a <= i:
                ave = t / i
                if ret < ave:
                    max_i = {i}
                    ret = ave
                elif ret == ave:
                    max_i.add(i)
            if i == b:
                break
        return ret, max_i

    @lru_cache(maxsize=None)
    def combination(n, r):
        if n < r or r < 0:
            return 0
        if r > n - r:
            return combination(n, n - r)
        if r == 0:
            return 1
        if r == 1:
            return n
        return combination(n - 1, r - 1) * n // r

    max_, indices = max_ave_x()

    ret = 0

    c1 = Counter(v)
    for i in indices:
        c2 = Counter(v[:i])
        t = 1
        for chr_ in c2:
            t *= combination(c1[chr_], c2[chr_])
        ret += t

    return max_, ret


print(*solve(), sep='\n')