# coding: utf-8

# https://atcoder.jp/contests/abc092/tasks/arc093_a
# 16:37-16]53 done


def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = [None] * N
    S[0] = abs(A[0])
    a = S[0]
    for i in range(1, N):
        a += abs(A[i]-A[i-1])
        S[i] = a

    print(S[N-1]-(abs(A[1]-A[0])+abs(A[0]))+abs(A[1])+abs(A[N-1]))

    for i in range(1, N-1):
        print(S[N-1]-(S[i+1]-S[i-1])+abs(A[i+1]-A[i-1])+abs(A[N-1]))

    print(S[N-2]+abs(A[N-2]))


main()
