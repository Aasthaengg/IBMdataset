N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
result = [0]
for i in range(N):
    D = D + L[i]
    if D>X:
        print(i+1)
        quit()
print(N+1)
