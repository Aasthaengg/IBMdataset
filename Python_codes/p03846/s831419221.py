import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N % 2 != 0:
        d = {2 * i: 0 for i in range(N // 2 + 1)}
        for a in A:
            try:
                d[a]  += 1
            except:
                print(0)
                return
        if d[0] != 1:
            print(0)
            return
        for key in d:
            if key == 0: continue
            if d[key] != 2:
                print(0)
                return
    else:
        d = {2 * i + 1: 0 for i in range(N // 2)}
        for a in A:
            try:
                d[a] += 1
            except:
                print(0)
                return
        for key in d:
            if d[key] != 2:
                print(0)
                return
    print(pow(2, N // 2, mod))

if __name__ == "__main__":
    main()
