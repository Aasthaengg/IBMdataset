H, W, A, B = input().strip().split()
H, W, A, B = [int(H), int(W), int(A), int(B)]

for i in range(B): # i = 0, 1, ..., B-1
    print('1' * A + '0' * (W - A))

for i in range(H-B):
    print('0' * A + '1' * (W - A))