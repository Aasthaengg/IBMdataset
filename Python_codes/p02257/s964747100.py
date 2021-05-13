# Fermat's little theorem
def is_prime(x):
    if x == 2:
        return 1
    elif x % 2 == 0:
        return 0
    else:
        return pow(2, x - 1, x) == 1

import sys

def solve():
    file_input = sys.stdin
    N = file_input.readline()
    cnt = 0
    for n in map(int, file_input):
        cnt += is_prime(n)
    print(cnt)

solve()