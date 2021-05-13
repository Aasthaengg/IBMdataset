# https://atcoder.jp/contests/tenka1-2018-beginner/submissions/6799589
# combinationを使うところ

def main():
    from itertools import combinations

    N = int(input())

    # {1,...,N}*2を分割
    # k個の集合があって
    # 各集合は他のk-1個の集合に対し共通要素を1個ずつ合わせてk-1個の要素をもつ

    k = 1
    while (k - 1) * k < N * 2:
        k += 1
    cond = (k - 1) * k == N * 2

    if not cond:
        print('No')
        return

    sets = tuple(set() for _ in range(k))
    for common_component, (set_idx_1, set_idx_2) in enumerate(combinations(range(k), r=2), start=1):
        sets[set_idx_1].add(common_component)
        sets[set_idx_2].add(common_component)

    print('Yes')
    print(k)
    for set_ in sets:
        print(len(set_), *set_)


if __name__ == '__main__':
    main()
