_, _, X, Y = map(int, input().split())
x = max(map(int, input().split()))
y = min(map(int, input().split()))

for z in range(X + 1, Y + 1):
    if x < z <= y:
        print("No War")
        break
else:
    print("War")