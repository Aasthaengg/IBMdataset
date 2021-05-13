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

    a, b ,c = get_int_multi()
    k = get_int()

    n2 = a / b
    m2 = math.floor(math.log(n2,2) +1)
    if m2 < 0:
        m2 = 0

    n1 = (b * pow(2, m2)) / c
    m1 = math.floor(math.log(n1,2) +1)
    if m1 < 0:
        m1 = 0

    if k >= m1+m2:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()


