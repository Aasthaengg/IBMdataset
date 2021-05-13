# -*- coding: utf-8 -*-
# スペース区切りの整数の入力
#N, K = map(int, input().split())
# 文字列の入力
N = int(input())
#開業されたN個要素を受け付ける
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    if A[i] <= B[i]:
        ans = ans+A[i]
        B[i] = B[i] - A[i]
        A[i] = 0
        if A[i+1] <= B[i]:
            ans = ans+A[i+1]
            B[i] = B[i] - A[i+1]
            A[i+1] = 0
        else:
            ans = ans+B[i]
            A[i+1] = A[i+1] - B[i]
            B[i] = 0
    else:
        ans = ans+B[i]
        A[i] = A[i] - B[i]
        B[i] = 0
    #print(A)
    #print(B)
    #print(ans)
    #print()

print(ans)
