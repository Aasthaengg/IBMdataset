def resolve():
    N = int(input())
    H = list(map(int, input().split()))
    c = 0
    d = c
    for i in range(N-1):
        if H[i] >= H[i+1]:
            c += 1
        else:
            d = max([c, d])
            c = 0
            
    print(max([c, d]))

resolve()