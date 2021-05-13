H,W,A,B = list(map(int,input().split()))
M = [[0]*W for _ in range(H)]



for ih in range(H):
    for iw in range(W):
        if (ih<B and iw <A) or (ih>=B and iw >= A):
            M[ih][iw] = 1
for i in range(H):
    print(''.join(list(map(str,M[i]))))

