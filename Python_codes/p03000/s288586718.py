N, X = map(int, input().split())
L = list(map(int, input().split()))
D = 0
for i in range(2, N + 2):
    if D + L[i - 2] > X:
        print(i - 1)
        break
    D = D + L[i - 2]
else:
    print(i)
