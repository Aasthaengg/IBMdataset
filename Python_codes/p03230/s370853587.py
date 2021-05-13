N = int(input())
k = int((2*N)**0.5)+1
if k*(k-1)==2*N:
    print('Yes')
    print(k)
    S = [[0 for j in range(k-1)] for i in range(k)]
    sx,sy = 0,0
    n = 1
    while sx<k:
        for i in range(k-1-sx):
            S[sx][sy+i] = n+i
            S[sx+1+i][sy] = n+i
        n += k-1-sx
        sx += 1
        sy += 1
    for s in S:
        print(len(s),*s)
else:
    print('No')