N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
if X < min(y) <= Y and min(y) - max(x) >= 1:
    print("No War")
else:
    print("War")
