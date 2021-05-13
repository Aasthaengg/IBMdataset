_, _, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

xmax = max(x)
ymin = min(y)
if xmax >= ymin:
    print("War")
else:
    for z in range(xmax+1, ymin+1):
        if X < z <= Y:
            print("No War")
            break
    else:
        print("War")
