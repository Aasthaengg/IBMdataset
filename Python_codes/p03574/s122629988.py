def p(h,w):
    try:
        if h >= 0 and h<= H and w >= 0 and w <= W:
            S[h][w] += 1
    except:
        None

H,W = map(int,input().split())
S = [[0 if i == "." else "#" for i in input()] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            p(i+1, j)
            p(i+1, j+1)
            p(i+1, j-1)
            p(i-1, j)
            p(i-1, j+1)
            p(i-1, j-1)
            p(i, j+1)
            p(i, j-1)
            '''
            for k in S:
                a = list(map(str, k))
                print("".join(a))
            print()
            '''
        else:
            None
for k in S:
    a = list(map(str,k))
    print("".join(a))