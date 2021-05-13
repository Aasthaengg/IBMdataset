#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt_P = 0
    cnt_N = 0

    for i in range(N):
        diff = B[i]-A[i]
        if diff>0:
            cnt_P += diff//2
        elif diff<0:
            cnt_N += -diff

    if sum(A)<=sum(B) and cnt_P>=cnt_N:
        ret = 'Yes'
    else:
        ret = 'No'

    print(ret)

if __name__ == '__main__':
    main()