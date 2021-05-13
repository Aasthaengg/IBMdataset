import copy
import math
import time
import statistics
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

    n, m = get_int_multi()

    s = []

    for i in range(m):
        wk = get_int_list()
        wk = wk[1:]
        s.append(wk)

    p = get_int_list()

    ans = 0
    for i in range(2 ** n):
        ok = True
        for ii in range(m): # 電球ごとに調査
            count = 0
            for iii in range(n): # スイッチONOFF
                if ((i >> iii) & 1):
                    if (iii+1) in s[ii]:
                        count += 1
            if (count % 2 != p[ii]):
                ok = False
                break
        if ok:
            ans += 1

    print(ans)



if __name__ == '__main__':
    main()


