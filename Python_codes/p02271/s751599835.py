# -*- coding: utf-8 -*-


def check_solvable_recursively(number, is_solvable, candidate_numbers):
    """exhaustively search representable as summation of numbers in candidate_numbers

    Args:
        number: representable number
        is_solvable: is solvable list
        candidate_numbers: candidate numbers to be used

    Returns:
        None
    """
    is_solvable[number] = True
    if candidate_numbers:
        check_solvable_recursively(number + candidate_numbers[0], is_solvable, candidate_numbers[1:])
        check_solvable_recursively(number, is_solvable, candidate_numbers[1:])
    else:
        pass


def main():
    raw_input()  # pass length
    candidate_numbers = [int(x) for x in raw_input().strip().split(' ')]
    raw_input()  # pass length
    target_number_list = [int(x) for x in raw_input().strip().split(' ')]

    is_solvable_list = [False] * 2001

    check_solvable_recursively(0, is_solvable_list, candidate_numbers)

    for target_number in target_number_list:
        if is_solvable_list[target_number]:
            print "yes"
        else:
            print "no"

if __name__ == "__main__":
    main()