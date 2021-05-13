# ABC 58 A

import numpy as np

def resolve():
    a, b, c = map(int, input().split())
    if b - a == c - b:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    resolve()
