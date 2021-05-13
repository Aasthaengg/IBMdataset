A, B, K = map(int, input().split())

takahasi_turn = 1
for _ in range(K):
    if takahasi_turn:
        if A % 2 == 1:
            A -= 1
        v = A // 2
        B += v
        A -= v
    else:
        if B % 2 == 1:
            B -= 1
        v = B // 2
        A += v
        B -= v
    takahasi_turn ^= 1
print(*[A, B])
