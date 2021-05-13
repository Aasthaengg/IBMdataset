def solve():
    H,W,A,B=map(int,input().split())
    data=[[0]*W for i in range(H)]
    for i in range(B):
        for j in range(A):
            data[i][j]=1
    for i in range(B,H):
        for j in range(A,W):
            data[i][j]=1
    return data

data=solve()
for i in data:
    print(''.join(map(str,i)))