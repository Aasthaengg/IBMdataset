A, B = map(int, input().split())
for i in range(20):
    if (A*i-(i-1) >= B ):
        print(i)
        exit(0)