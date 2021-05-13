#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    B = list(map(int,input().split()))
    ret = []
    while len(B)>0:
        for j in range(len(B)-1,-1,-1):
            if B[j]==j+1:
                ret.append(j+1)
                B.pop(j)
                break
            if j==0 and B[j]!=(j+1):
                print(-1)
                exit()
    print('\n'.join(map(str,ret[::-1])))


if __name__ == '__main__':
    main()