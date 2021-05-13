# B - 1 Dimensional World's Tale
N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

ans = "War"

for Z in range(-100,101):
    if max(x) < Z <= min(y):
        if X < Z <= Y:
            ans = "No War"
            break

print(ans)