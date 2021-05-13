import collections


def main():
    N = int(input())
    table = [''.join(sorted(list(input()))) for _ in range(N)]
    sort_table = set(table)
    cnt_table = collections.Counter(table)
    ans = 0
    for i in sort_table:
        num_of_i = cnt_table[i]
        if num_of_i <= 1:
            continue
        x = (num_of_i * (num_of_i - 1)) // 2
        ans += x

    print(ans)


if __name__ == '__main__':
    main()
