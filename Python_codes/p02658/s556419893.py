from functools import reduce
from operator import mul
import math

def main():
    n = int(input())
    l = list(map(int, input().split()))

    if 0 in l:
        print(0)
        return
    l_sorted = sorted(l, reverse=True)
    log = 0
    seki = 1
    for i in l_sorted:
        log += math.log10(i)
        if log > 18:
            print(-1)
            return
        elif log == 18:
            seki *= i
            if seki != 10 ** 18:
                print(-1)
                return
        else:
            seki *= i
    print(seki)
    return


if __name__ == '__main__':
    main()