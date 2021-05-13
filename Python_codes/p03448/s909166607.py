import itertools
import pprint

a = int(input())
b = int(input())
c = int(input())
x = int(input())

a_list = [i for i in range(a + 1)]
b_list = [i for i in range(b + 1)]
c_list = [i for i in range(c + 1)]

ans = 0
for a_num, b_num, c_num in itertools.product(a_list, b_list, c_list):
    # print(500 * a_num + 100 * b_num + 50 * c_num)
    if x == 500 * a_num + 100 * b_num + 50 * c_num:
        ans += 1
print(ans)