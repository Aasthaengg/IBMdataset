def resolve():
    n = int(input())
    H = list(map(int, input().split()))
    max_c = 0
    c = 0
    for i in range(n-1):
        now = H[i]
        nxt = H[i+1]
        if now >= nxt:
            c += 1
        else:
            max_c = max(max_c, c)
            c = 0
    print(max(max_c,c)) 
resolve()