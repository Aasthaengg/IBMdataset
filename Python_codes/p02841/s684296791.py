MD = [map(int, input().split()) for _ in range(2)]
M, D = [list(i) for i in zip(*MD)]

if D[1] == 1:
    print(1)
else:
    print(0)