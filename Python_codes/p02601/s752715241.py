def main():
    A, B, C = input_ints()
    K = input_ints()

    while K > 0:
        if A >= B:
            B *= 2
        elif B >= C:
            C *= 2

        K -= 1

    if A < B < C:
        print('Yes')
    else:
        print('No')


def input_ints():
    line_list = input().split()

    if len(line_list) == 1:
        return int(line_list[0])
    else:
        return map(int, line_list)


def input_int_list_in_line():
    return list(map(int, input().split()))


def input_int_tuple_list(n: int):
    return [tuple(map(int, input().split())) for _ in range(n)]


main()
