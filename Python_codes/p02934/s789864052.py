import numpy as np
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    for i in a:
        tmp += 1/i
    print(1/tmp)

if __name__ == '__main__':
    solve()
