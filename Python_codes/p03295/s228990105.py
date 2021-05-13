import sys
import math

def resolve():
    N, M = list(map(int, input().split()))
    AB = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x: x[1])
    broken = None
    cnt = 0
    for ab in AB:
        a, b = ab
        if broken and a <= broken < b:
            continue
        broken = b-1
        cnt += 1
    print(cnt)

    

if '__main__' == __name__:
    resolve()