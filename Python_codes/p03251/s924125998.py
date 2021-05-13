def resolve():
    _, _, X, Y = [int(i) for i in input().split()]
    xx = sorted([int(i) for i in input().split()] + [X])
    yy = sorted([int(i) for i in input().split()] + [Y])
    if xx[-1] >= yy[0]:
        print("War")
    else:
        print("No War")

resolve()
