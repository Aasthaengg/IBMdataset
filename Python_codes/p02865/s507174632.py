import os
import numpy as np

class getStdin(object):
    @classmethod
    def get_int(cls):
        return int(input())

    @classmethod
    def get_ss_int(cls):
        return list(map(int, input().split()))

    @classmethod
    def get_na_int(cls):
        return np.array(sorted(list(map(int, input().split()))))

    @classmethod
    def get_na_intr(cls):
        return np.array(sorted(list(map(int, input().split())))[::-1])

if __name__ == '__main__':
    n = getStdin.get_int()
    if n % 2 == 0:
        print(n//2 -1)
    else:
        print(n//2)
    os.sys.exit(0)