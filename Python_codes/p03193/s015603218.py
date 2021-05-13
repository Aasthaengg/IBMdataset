n, h, w = [int(i) for i in input().split(" ")]
n_boards = 0
for k in range(n):
    hi, wi = [int(i) for i in input().split(" ")]
    if hi >= h and wi >= w:
        n_boards += 1
print(n_boards)