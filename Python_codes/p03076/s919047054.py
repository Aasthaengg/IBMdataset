def multiple_of_ten(number):
    while number % 10 != 0:
        number += 1
    return number


def max_difference_between_two_lst(lst1, lst2):
    difference_lst = []
    for i in range(len(lst1)):
        number1 = lst1[i]
        number2 = lst2[i]
        difference_lst.append(abs(number1 - number2))
    max_difference = max(difference_lst)
    return max_difference


def main():
    time_lst = []
    for _ in range(5):
        time_lst.append(int(input()))

    new_time_lst = []
    for i in range(5):
        time = time_lst[i]
        new_time_lst.append(multiple_of_ten(time))

    max_difference = max_difference_between_two_lst(time_lst, new_time_lst)
    fastest = sum(new_time_lst) - max_difference
    print(fastest)


if __name__ == '__main__':
    main()