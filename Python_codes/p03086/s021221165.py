import copy
import math

# a = get_int()
def get_int():
    return int(input())
# a = get_string()
def get_string():
    return input()
# a_list = get_int_list()
def get_int_list():
    return [int(x) for x in input().split()]
# a_list = get_string_list():
def get_string_list():
    return input().split()
# a, b = get_int_multi()
def get_int_multi():  # a, b = get_int_multi()
    return map(int, input().split())
# a_list = get_string_char_list()
def get_string_char_list():
    return list(str(input()))
# print("{} {}".format(a, b))
# for num in range(0, a):
# a_list[idx]
# a_list = [0] * a
'''
while (idx < n) and ():

    idx += 1
'''

def main():

    a_list = get_string_char_list()
    ans = 0
    count = 0
    for s in a_list:

        if s in ("A","C","G","T"):
            count += 1
            ans = max(ans, count)
        else:
            count = 0
    print(ans)

if __name__ == '__main__':
    main()


