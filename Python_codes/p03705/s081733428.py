N, A, B = map(int,input().split())
min = A * (N - 1) + B
max = B * (N - 1) + A
if (max - min) + 1 < 0:
    print("0")
else:
    print((max - min) + 1)