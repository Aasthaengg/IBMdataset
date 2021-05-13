from collections import defaultdict


def main():
    S = input()
    N = len(S)
    index_list_dict = defaultdict(list)
    for i, c in enumerate(S):
        index_list_dict[c].append(i)
    ans = N
    for index_list in index_list_dict.values():
        li = [-1] + index_list + [N]
        v = 0
        for i in range(len(li) - 1):
            v = max(v, li[i + 1] - li[i] - 1)
        ans = min(ans, v)
    print(ans)


if __name__ == '__main__':
    main()
