# 君指先跃动の光は、私の一生不変の信仰に、唯私の超电磁炮永生き！
from sys import stdin, stdout
import math
import bisect
from collections import defaultdict
import datetime
import random

# n = int(stdin.readline().strip())
# arr = list(map(int, stdin.readline().strip().split()))

n, m = map(int, stdin.readline().strip().split())

if m == 1:
    stdout.writelines('1 2\n')
else:
    m1 = m // 2
    m2 = m - m1
    a = m2
    b = a + 1
    for i in range(m2):
        stdout.writelines('%d %d\n' % (a, b))
        a -= 1
        b += 1
    a = b
    b = a + m1 * 2
    for i in range(m1):
        stdout.writelines('%d %d\n' % (a, b))
        a += 1
        b -= 1
