from decimal import *

n = int(input())
T, A = [], []
for _ in range(n):
    t, a = map(int, input().split())
    T.append(t)
    A.append(a)

Taka = 0
Aoki = 0

for i in range(n):

    if (T[i] >= Taka) and (A[i] >= Aoki):
        Taka = T[i]
        Aoki = A[i]
    elif T[i] == A[i]:
        Taka = max(Taka, Aoki)
        Aoki = Taka
    else:
        Taka_up = -(-Taka//T[i])
        Aoki_up = -(-Aoki//A[i])
        multi = max(Taka_up, Aoki_up)
        Taka = T[i] * multi
        Aoki = A[i] * multi   

ans = int(Taka + Aoki)
print(ans)