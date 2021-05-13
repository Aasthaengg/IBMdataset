import sys
def main():
    input = sys.stdin.readline
    H,W=map(int, input().split())
    A=[list(input().rstrip()) for _ in range(H)]
    from itertools import chain
    from collections import Counter
    C=Counter(chain.from_iterable(A))
    t4=[(v//4)*4 for v in C.values()]
    t2=[(v//2)*2 for v in C.values()]
    if sum(t4) >= (H-(H&1))*(W-(W&1)):
        if sum(t2) >= H*W-(H&W&1):
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()