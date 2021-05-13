M = 3501
N = int(input())
for h in range(1, M):
    for w in range(1, M):
        u = 4*h*w-N*w-N*h
        d = N*h*w
        if u <= 0:
            continue
        if d % u == 0:
            print(h, w, d//u)
            exit()
