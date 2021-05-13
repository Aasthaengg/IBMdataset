A, B, C, D = list(map(int, input().split()))

rec_a = A * B
rec_b = C * D

if rec_a >= rec_b:
    print(rec_a)
else :
    print(rec_b)