import numpy as np

def yakusu(n):
    a = []
    for i in range(1, int(n*0.5)+1):
        if n % i == 0:
            a.append(i)
    a.append(n)
    return a

A, B, K = map(int, input().split())
a = yakusu(A)
b = yakusu(B)
ab = []
for i in a:
    if i in b:
        ab.append(i)
print(ab[-1*K])