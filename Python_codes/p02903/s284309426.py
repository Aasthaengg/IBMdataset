h, w, a, b = map(int, input().split())

ans = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if (i < b and j >= a) or (i >= b and j < a):
            print(1, end = "")
        else:
            print(0, end = "")
    
    print()
