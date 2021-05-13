H,W,A,B = map(int,input().split())
lis = [['0'] * W for i in range(H)]

for i in range(H):
    if i < B:
        for j in range(A,W):
            lis[i][j] = '1'
    else:
        for j in range(A):
            lis[i][j] = '1'
for i in lis:
    print(''.join(i))
