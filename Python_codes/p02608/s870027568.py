# coding: utf-8

N = int(input())

ANS = [0] * (N+1)

for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            a = i**2 + j**2 + k**2 + i*j + j*k + k*i
            if a <= N:
                ANS[a] += 1

for i in range(1,N+1):
    print(ANS[i])