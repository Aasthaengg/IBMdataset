#!/usr/bin/env python3
import sys


def solve(N: int, D: int):
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N,D = [ int(s) for s in input().split() ]
    if N % (2*D+1) == 0:
        print(int(N / (2*D+1)))
    else:
        print(int(N / (2*D+1))+ 1)

    

if __name__ == '__main__':
    main()