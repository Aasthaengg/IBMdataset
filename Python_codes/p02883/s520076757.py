import sys
import numpy as np
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    a = np.array(sorted(list(map(int, input().split()))))
    f = np.array(sorted(list(map(int, input().split())), reverse=True))

    Asum = a.sum()

    l, r = 0, int(1e13)
    while l != r:
        p = (l + r) // 2
        tmp = Asum - np.minimum(a, p//f).sum() <= K
        # print(p, tmp)
        if tmp:
            r = p
        else:
            l = p + 1
    
    print(l)


if __name__ == "__main__":
    main()