N = int(input())
D, X = map(int,input().split())

for i in range(N):
    A = int(input())
    j = 0
    while j * A + 1 <= D:
        X += 1
        j += 1

print(X)