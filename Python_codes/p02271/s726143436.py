# -*- coding: utf-8 -*-


def main():
    raw_input()  # pass length
    candidate_number_list = [int(x) for x in raw_input().strip().split(' ')]
    raw_input()  # pass length
    target_number_list = [int(x) for x in raw_input().strip().split(' ')]

    representable_number_set = {0}
    for candidate_number in candidate_number_list:
        for num in representable_number_set.copy():
            representable_number_set.add(num + candidate_number)

    for target_number in target_number_list:
        if target_number in representable_number_set:
            print "yes"
        else:
            print "no"

if __name__ == "__main__":
    main()