import sys
import math

def resolve():
    N = int(input())
    mods = []
    target = N
    if N == 0:
        print("0")
        return
    while True:
        if target == 1:
            mods.append("1")
            break
        v = target // (-2)
        c = target % (-2)
        if c == -1:
            v += 1
            c = 1
        mods.append(str(c))
        target = v
    mods.reverse()
    print("".join(mods))

if '__main__' == __name__:
    resolve()