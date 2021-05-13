# -*- coding: utf-8 -*-
import sys


def main():
    K = int( sys.stdin.readline() )
 
    A = 7

    for i in range(K):
        if A % K == 0:
            print(i+1)
            return

        A = (A * 10) + 7
        A %= K
    
    print(-1)


if __name__ == "__main__":
    main()
