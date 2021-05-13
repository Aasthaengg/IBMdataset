H, W, A, B = map(int, input().split())
if W<=A or H<=B:
    print("No")
    exit()
K = "1"*A + "0"*(W-A)
L = "0"*A + "1"*(W-A)
for i in range(H):
    if i <= B-1:
        print(K)
    else:
        print(L)