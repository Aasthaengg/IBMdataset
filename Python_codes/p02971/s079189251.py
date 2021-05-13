def main():
    n = int(input())
    a_lst = [int(input()) for i in range(n)]
    a_lst_descend = sorted(a_lst, reverse=True)

    max_value = a_lst_descend[0]
    second_value = a_lst_descend[1]

    for a in a_lst:
        if a == max_value:
            print(second_value)
        else:
            print(max_value)


if __name__ == "__main__":
    main()
