# https://atcoder.jp/contests/abc106/tasks/abc106_b
import math

N = int(input())


def is_8(num):
    if num < 1:
        return False
    elif num == 1:
        return False
    else:
        divisor_list = set()
        divisor_list.add(1)
        # root nまで見れば問題ない
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisor_list.add(num // i)
                divisor_list.add(i)
        # 元の数を入れる
        divisor_list.add(num)
        if len(divisor_list) == 8:
            return True

cnt = 0
for i in range(1, N + 1, 2):
    if is_8(i):
        cnt += 1

print(cnt)
