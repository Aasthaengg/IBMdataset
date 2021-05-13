h, w, a, b = map(int, input().split())
for i in range(h):
    for j in range(w):
        print(int((j < a) ^ (i < b)), end='')
    print()