n, p = map(int, input().split())
a = list(map(int, input().split()))
os = list(filter(lambda x: x % 2 == 1, a))
es = list(filter(lambda x: x % 2 == 0, a))

def calc_even(o_num, e_num):
    if o_num < 0 or e_num < 0:
        return 0
    # 奇数の組み合わせ数
    res = 1
    tmp = 1
    for i in range(1, o_num // 2 + 1):
        tmp *= (o_num - i * 2 + 2) * (o_num - i * 2 + 1)
        tmp /= 2 * i * (2 * i - 1)
        res += tmp
    # 偶数の組み合わせ数
    res *= 2 ** e_num
    return res

def calc_odd(o_num, e_num):
    if o_num < 0 or e_num < 0:
        return 0
    # 奇数の組み合わせ数
    tmp = o_num
    res = tmp
    end = o_num if o_num % 2 == 1 else o_num-1
    for i in range(1, end // 2 + 1):
        tmp *= (o_num - i * 2 + 1) * (o_num - i * 2)
        tmp /= 2 * i * (2 * i + 1)
        res += tmp
    # 偶数の組み合わせ数
    res *= 2 ** e_num
    return res
if p == 0:
    res = calc_even(len(os), len(es))
    print(int(res))
else:
    res = calc_odd(len(os), len(es))
    print(int(res))