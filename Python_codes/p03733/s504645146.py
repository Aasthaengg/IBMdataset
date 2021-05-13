N, T = map(int, input().split())
L = [int(i) for i in input().split()]
x = 0

for i in range(N-1):
    if L[i+1] - L[i] >= T:
        x += T
    else:
        x += L[i+1] - L[i]
else:
    x += T
    print(x)
