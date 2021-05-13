h, w, a, b = map(int, input().split())

for i in range(h):
    for j in range(w):
        if i < (h-b):
            if j < (w-a):
                print(0, end="")
            else:
                print(1, end="")
        else:
            if j < (w-a):
                print(1, end="")
            else:
                print(0, end="")
    print('')