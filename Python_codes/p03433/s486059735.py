# coding: utf-8
N = int(input())
A = int(input())

B = N // 500
if N - B * 500 <= A :
    print('Yes')
else:
    print('No')