#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    mod=998244353
    n, k = map(int, input().split())
    lr = []
    for i in range(k):
        l, r = map(int, input().split())
        lr.append((l, r))
    ans=[1]
    acc_ans=[1]
    for i in range(1, n):
        wa = 0
        for l, r in lr:
            if i-r > 0:
                wa+=-acc_ans[i-r-1]+acc_ans[i-l]
            elif i-l>=0:
                wa+=acc_ans[i-l]
        wa%=mod
        ans.append(wa)
        acc_ans.append(wa+acc_ans[-1])
    print(ans[-1])


if __name__ == '__main__':
    main()
