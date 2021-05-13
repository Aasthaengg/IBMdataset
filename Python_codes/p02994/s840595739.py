def the_closest_number_to_zero(lst):
    positive_lst = []
    negative_lst = []
    zero_lst = []
    n = len(lst)

    for i in range(n):
        number = lst[i]

        if number == 0:
            zero_lst.append(number)
        elif number > 0:
            positive_lst.append(number)
        else:
            negative_lst.append(number)

    if len(zero_lst) != 0:
        the_closest_number = 0
    else:
        positive_lst = sorted(positive_lst)
        negative_lst = sorted(negative_lst)

        if len(positive_lst) == 0:
            the_closest_number = negative_lst[-1]
        elif len(negative_lst) == 0:
            the_closest_number = positive_lst[0]
        else:
            positive = positive_lst[0]
            negative = negative_lst[-1]
            if abs(positive) >= abs(negative):
                the_closest_number = negative
            else:
                the_closest_number = positive

    return the_closest_number


def main():
    n, l = map(int, input().split())
    taste_lst = []

    for i in range(n):
        taste_lst.append(l+i)

    taste_total = sum(taste_lst)
    taste_bite = the_closest_number_to_zero(taste_lst)
    taste = taste_total - taste_bite

    print(taste)


if __name__ == '__main__':
    main()