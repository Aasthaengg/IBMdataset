# input here
_INPUT = """\
2 5
1 WA
1 AC
2 WA
2 AC
2 WA
2 AC
"""

def main():
    n, m = map(int, input().split())

    seikai = [False] * n
    matigai = [0] * n

    for i in range(m):
        p,q = map(str, input().split())
        p = int(p)-1

        if q == "AC":
            seikai[p] = True
        else:
            if seikai[p] != True:
                matigai[p] += 1

    num = 0
    ac = 0
    for i in range(n):
        if seikai[i] == True:
            num += matigai[i]
            ac += 1
    print(ac,num)
            
if __name__ == '__main__':
    import io
    import sys
    import math
    import itertools
    from collections import deque

    # sys.stdin = io.StringIO(_INPUT)
    main()