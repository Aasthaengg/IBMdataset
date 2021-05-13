from itertools import chain, combinations


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def s_to_num(s):
    numlst = list(map(int, s))
    res = 0
    for i in numlst:
        res *= 10
        res += i
    return res


s = input()
length = len(s)
res = 0
for i in powerset(range(1, length)):
    if not i:
        res += int(s)
    else:
        jlst = [0] + list(i) + [length]
        for j in range(len(jlst) - 1):
            res += s_to_num(s[jlst[j]:jlst[j + 1]])
print(res)
