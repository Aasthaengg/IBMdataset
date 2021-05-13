def abc137c_green_bin():
    def cmb(n, r):
        """ nCrの組み合わせ数を返す """
        if n - r < r: r = n - r
        if r == 0: return 1
        if r == 1: return n

        numerator = [n - r + k + 1 for k in range(r)]
        denominator = [k + 1 for k in range(r)]

        for p in range(2,r+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (n - r) % p
                for k in range(p-1,r,p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(r):
            if numerator[k] > 1:
                result *= int(numerator[k])

        return result
    n = int(input())
    dict_s = {}
    for _ in range(n):
        s = ''.join(sorted(input()))
        if s in dict_s.keys():
            dict_s[s] += 1
        else:
            dict_s[s] = 1
    result = 0
    for k in dict_s:
        if dict_s[k] != 1:
            result += cmb(dict_s[k], 2)
    print(result)
abc137c_green_bin()