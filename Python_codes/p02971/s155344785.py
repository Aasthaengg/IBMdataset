n = int(input())
A = [int(input()) for _ in range(n)]
ma_1 = max(A)
ma_2 = sorted(A)[-2]
for a in A:
    if a == ma_1:
        print(ma_2)
    else:
        print(ma_1)