import copy

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

    n = get_int()
    a_list = get_int_list()

    w_min = a_list[0]
    w_max = a_list[0]
    pre = a_list[0]
    kabu = 0
    kane = 1000

    for i in range(1, n):

        if pre < a_list[i] and kabu == 0:
            kabu = kane // w_min
            kane = kane - kabu * w_min
            w_max = a_list[i]

        elif pre > a_list[i] and kabu > 0:
            kane = kane + w_max * kabu
            kabu = 0
            w_min = a_list[i]

        elif pre < a_list[i] and kabu > 0:
            w_max = a_list[i]

        elif pre > a_list[i] and kabu == 0:
            w_min = a_list[i]



        pre = a_list[i]

    if kabu > 0:
        kane = kane + w_max * kabu

    print(kane)






if __name__ == '__main__':
    main()


