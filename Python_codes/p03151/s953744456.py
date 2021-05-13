import sys
import numpy as np
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    A = np.array(readline().split(), np.int64)
    B = np.array(readline().split(), np.int64)
    C = A-B
    pos = C[C>0]
    neg = C[C<0]
    Lpos = len(pos)
    Lneg = len(neg)
    pos = np.sort(pos)[::-1]
    total = np.sum(neg)
    if Lneg == 0:
        print(0)
        sys.exit()
    for i in range(Lpos):
        total += pos[i]
        if total>=0:
            print(Lneg+i+1)
            break
        else:
            continue
    else:
        print(-1)




if __name__ == '__main__':
    main()
