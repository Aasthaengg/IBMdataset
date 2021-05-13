def main():
    n = int(input())
    a_lst = [(int(input()), i + 1) for i in range(n)]
    a_lst_descend = sorted(a_lst, reverse=True)

    max_value = a_lst_descend[0][0]
    max_index = a_lst_descend[0][1]
    second_value = a_lst_descend[1][0]

    for i in range(1, n + 1):
        if i == max_index:
            print(second_value)
        else:
            print(max_value)


if __name__ == "__main__":
    main()
