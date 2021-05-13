H, W, A, B = map(int, input().split())

if H == 1:
    ans = "1"*A + "0"*(W-A)
    print(ans)
    exit()

if W == 1:
    for _ in range(B):
        print(1)
    for _ in range(H-B):
        print(0)
    exit()

ans = [[0]*W for _ in range(H)]

for i in range(B):
    for j in range(A):
        ans[i][j] = 1

for i in range(B, H):
    for j in range(A, W):
        ans[i][j] = 1

for a in ans:
    t = list(map(str, a))
    print("".join(t))