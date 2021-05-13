a, b, k = [int(i) for i in input().split()]
turn = 0
for i in range(k):
    if turn == 0:
        a = a//2
        b += a
        turn = 1
    elif turn == 1:
        b = b//2
        a += b
        turn = 0
print(a, b)