judge = True

while judge:
    h,w = map(int, input().split(" "))
    if h == 0 and w == 0:
        judge = False
    else:
        for i in range(h):
            print("#" * w)
        print()