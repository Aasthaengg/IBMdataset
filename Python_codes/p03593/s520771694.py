from collections import defaultdict

H,W = map(int,input().split())
a = [[] for _ in range(H)]
for i in range(H):
    a[i] = list(input())

d = defaultdict(int)
for i in range(H):
    for j in range(W):
        d[a[i][j]] += 1

c4,c2 = 0,0
for k in d.keys():
    c4 += d[k]//4
    c2 += (d[k]%4)//2

if H%2 + W%2 == 0:
    if c4 == H*W//4:
        print("Yes")
    else:
        print("No")
elif H%2 + W%2 == 1:
    if H%2 == 1:
        if c4 < (H-1)*W//4:
            print("No")
        else:
            c4 -= (H-1)*W//4
            c2 += c4*2
            if c2 == W//2:
                print("Yes")
            else:
                print("No")
    if W%2 == 1:
        if c4 < H*(W-1)//4:
            print("No")
        else:
            c4 -= H*(W-1)//4
            c2 += c4*2
            if c2 == H//2:
                print("Yes")
            else:
                print("No")
else:
    if c4 < (H-1)*(W-1)//4:
        print("No")
    else:
        c4 -= (H-1)*(W-1)//4
        c2 += c4*2
        if c2 == (H-1)//2+(W-1)//2:
            print("Yes")
        else:
            print("No")