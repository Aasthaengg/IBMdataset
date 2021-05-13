H,W = map(int,input().split())
N = int(input())
A = list(map(int,input().split()))

ans = [[0 for w in range(W)] for h in range(H)]

for h in range(H):
    if h%2 == 0:
        for w in range(W):
            ans[h][w] = N
            A[-1] -= 1
            if A[-1] == 0:
                A.pop(-1)
                N -= 1
    else:
        for w in range(1,W+1):
            ans[h][(-1)*w] = N
            A[-1] -= 1
            if A[-1] == 0:
                A.pop(-1)
                N -= 1

for h in range(H):
    ans[h] = map(str,ans[h])
    print(' '.join(ans[h]))