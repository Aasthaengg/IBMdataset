H,W = map(int,input().split())
A = [input().strip() for _ in range(H)]
C = {chr(i):0 for i in range(97,123)}
for i in range(H):
    for j in range(W):
        C[A[i][j]] += 1
if H%2==0 and W%2==0:
    flag = 0
    for a in C:
        if C[a]%4!=0:
            flag = 1
            break
    if flag==0:
        print("Yes")
    else:
        print("No")
elif H%2==0 and W%2==1:
    cnt = 0
    flag = 0
    for a in C:
        if C[a]%4==2:
            cnt += 1
        elif C[a]%4!=0:
            flag = 1
            break
    if flag==1:
        print("No")
    else:
        if cnt<=H//2:
            print("Yes")
        else:
            print("No")
elif H%2==1 and W%2==0:
    flag = 0
    cnt = 0
    for a in C:
        if C[a]%4==2:
            cnt += 1
        elif C[a]%4!=0:
            flag = 1
            break
    if flag==1:
        print("No")
    else:
        if cnt<=W//2:
            print("Yes")
        else:
            print("No")
else:
    cnt1 = 0
    cnt2 = 0
    for a in C:
        if C[a]%4==2:
            cnt2 += 1
        elif C[a]%2==1:
            cnt1 += 1
    if cnt1!=1:
        print("No")
    else:
        if cnt2<=(H-1)//2+(W-1)//2:
            print("Yes")
        else:
            print("No")