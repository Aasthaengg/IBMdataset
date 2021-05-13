def count_list(lst):
    count_lst = [0] * (max(lst) + 2) #0からmax(lst)+1までの個数のリスト

    for i in lst:
        count_lst[i] += 1

    return count_lst


def main():
    n, k = map(int, input().split())
    a_lst = list(map(int, input().split()))
    new_lst = list(set(a_lst))
    types = len(new_lst)

    if types <= k:
        print(0)
    else:
        erase = types - k
        count_lst = count_list(a_lst)
        count_lst.sort()
        count = 0

        tmp = 0
        for i in count_lst:
            if i != 0:
                count += i
                tmp += 1

            if tmp == erase:
                break

        print(count)


if __name__ == '__main__':
    main()