a, b, c, k = map(int, input().split())

init_ = a - b

if abs(a - b) > 10**18:
    print("Unfair")
else:
    if k % 2 == 1:
        print(-(a - b))
    else:
        print(a - b)