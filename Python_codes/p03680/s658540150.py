def resolve():
    N = int(input())
    A = [int(input()) - 1 for _ in range(N)]

    pressed = 0
    i = 0
    t = 0
    while i != 1:
        i = A[i]
        if pressed > N:
            t = -1
            break
        pressed += 1
        t += 1

    print(t)
    
resolve()