# -*- coding: utf-8 -*-
def linear_search(value, target_list):
    for key in target_list:
        if value == key:
            return True
    return False


def main():
    s_length = raw_input()
    s = raw_input().strip().split(' ')
    t_length = raw_input()
    t = raw_input().strip().split(' ')


    counter = 0
    for t_value in t:
        counter += int(linear_search(t_value, s))

    print counter

if __name__ == '__main__':
    main()