N, A, B = list(map(int, input().split()))

# b = [None] * N
# b[A-1] = 'A'
# b[B-1] = 'B'

ans = ''
while True:
    if A + 1 == B:
        A -= 1
        if A == 0:
            ans = 'Borys'
            break
    else:
        A += 1

    if B - 1 == A:
        B += 1
        if B == N+1:
            ans = 'Alice'
            break
    else:
        B -= 1

print(ans)