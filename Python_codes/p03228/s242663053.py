A, B, K = map(int, input().split())
k = 0
while True:
    if k == K:
        break
    if A % 2 == 1:
        A -= 1
    B += A // 2
    A -= A // 2
    k += 1
    if k == K:
        break
    if B % 2 == 1:
        B -= 1
    A += B // 2
    B -= B // 2
    k += 1
print(A, B)