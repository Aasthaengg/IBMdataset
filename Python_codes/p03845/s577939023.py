# coding: utf-8
N = int(input())
T = list(map(int, input().split()))
M = int(input())
for i in range(M):
    P, X = map(int, input().split())
    M = [X if j + 1 == P else T[j] for j in range(N)]
    print(sum(M))