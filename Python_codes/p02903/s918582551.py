

H,W,A,B = map(int,input().split())

s = [['0']*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i>=B and j<A:
            s[i][j] = '1'
        elif i<B and j>=A:
            s[i][j] = '1'

for ss in s:
    tmps = ''.join(ss)
    print(tmps)
