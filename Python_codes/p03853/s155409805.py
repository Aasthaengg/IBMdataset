H,W=map(int,input().split())
C=[list(map(str,input().split())) for i in range(H)]
for i in range(2*H):
    print("".join(C[(i)//2]))