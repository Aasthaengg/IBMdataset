import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
import numpy as np

def scores(c, s, t):
    last = [0] * 26
    V = []
    lastv = 0
    for d, i in enumerate(t):
        last[i] = d+1
        v = s[d*26+i]
        sub = sum([c[j]*(d+1-last[j]) for j in range(26)])
        # print(v, sub)
        lastv += v-sub
        V.append(lastv)
    return V


def main():
    D, *cs = map(int, read().split())
    c = cs[:26]
    s = cs[26:-D]
    t = [x-1 for x in cs[-D:]]

    v = scores(c, s, t)
    print(*v, sep='\n')
    # c = cs[:26]
    # s = cs[26:]
    # print(D, c)
    # print(s)

if __name__ == '__main__':
    main()