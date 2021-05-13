import copy
import math
import time
import statistics
import math
import itertools

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
def get_int_multi():
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
    start = time.time()
    n = get_int()
    a = []
    ans = 0
    for i in range(n):
        a.append(get_int_list())

    count = 0
    for keiro in itertools.permutations(a):
        count += 1
        nagasa = 0
        for i in range(1,n):
            nagasa += math.sqrt((keiro[i][0] - keiro[i-1][0]) ** 2 + (keiro[i][1] - keiro[i-1][1]) **2)
        ans += nagasa
    print(ans / count)


if __name__ == '__main__':
    main()


