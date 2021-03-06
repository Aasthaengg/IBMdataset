# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
# 
# 
# @stop_watch
def solve(S, T):
    N = len(S)
    S_check = [0] * N
    T_check = [0] * N
    for i in range(N):
        if S_check[i] == 0:
            S_check[i] = 1
            for j in range(i + 1, N):
                if S[i] == S[j]:
                    S_check[j] = 1
                    if T[i] != T[j]:
                        print('No')
                        return
        if T_check[i] == 0:
            T_check[i] = 1
            for j in range(i + 1, N):
                if T[i] == T[j]:
                    T_check[j] = 1
                    if S[i] != S[j]:
                        print('No')
                        return
    print('Yes')


if __name__ == '__main__':
    S = input()
    T = input()
    solve(S, T)

    # # test
    # from random import randint
    # from func import random_str
    # S = 'abcdefghijklmnopqrstuvwxyz' * (2 * 10 ** 5 // 26 + 1)
    # T = 'abcdefghijklmnopqrstuvwxyz' * (2 * 10 ** 5 // 26 + 1)
    # solve(S, T)
