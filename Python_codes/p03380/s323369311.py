from operator import mul
from functools import reduce
import bisect
n = int(input())
A = sorted(list(map(int, input().split())))

big_num = A[-1]
near_mid_pointer = bisect.bisect_left(A, big_num / 2)
dif1 = 10**9 + 1
if near_mid_pointer != 0:
        dif1 = big_num / 2 - A[near_mid_pointer - 1]
dif2 = A[near_mid_pointer] - big_num / 2
if dif1 <= dif2:
    num1 = big_num
    num2 = A[near_mid_pointer - 1]

else:
    num1 = big_num
    num2 = A[near_mid_pointer]

print(num1, num2)