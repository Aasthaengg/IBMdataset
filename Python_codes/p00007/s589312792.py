
import math
import sys


def debt(debt_s, week):
    if week == 0:
        return debt_s
    debt_s = int(math.ceil((debt_s * 1.05)/1000) * 1000)
    return debt(debt_s, week - 1)


n = int(sys.stdin.readline())

debt_s = 100000
print debt(debt_s, n)