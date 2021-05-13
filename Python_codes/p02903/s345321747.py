H,W,A,B = map(int,input().split())
ans = [[0 for i in range(W)] for j in range(H)]

for h in range(B):
    for w in range(A,W):
        ans[h][w] = 1

for h in range(B,H):
    for w in range(A):
        ans[h][w] = 1

for a in ans:
    for n in a:
        print(n,end='')
    print() 