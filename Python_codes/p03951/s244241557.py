#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    S = input()
    T = input()

    ret = 2*N
    for i in range(N):
        if S[i:]==T[:N-i]:
            ret = 2*N-(N-i)
            break
    print(ret)



if __name__ == '__main__':
    main()