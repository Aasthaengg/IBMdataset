from collections import Counter
def solve():
    s = input()
    t = input()
    s_cnt = Counter(s)
    t_cnt = Counter(t)
    if all(sv == tv for sv, tv in zip(sorted(s_cnt.values()), sorted(t_cnt.values()))):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
