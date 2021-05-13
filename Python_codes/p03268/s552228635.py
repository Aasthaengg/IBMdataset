N, K =map(int, input().split())

mult = N//K
if K % 2 == 1:
    halfmult = 0
elif N % K < K//2:
    halfmult = mult
else:
    halfmult = mult + 1

print(mult**3 + halfmult**3)