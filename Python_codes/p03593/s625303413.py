H,W = map(int,input().split())
A = [input().strip() for _ in range(H)]
C = {}
for i in range(H):
    for j in range(W):
        a = A[i][j]
        if a not in C:
            C[a] = 0
        C[a] += 1
if H==1 or W==1:
    if H*W%2==0:
        flag = 0
        for a in C:
            if C[a]%2==1:
                flag = 1
                break
        if flag==0:
            print("Yes")
        else:
            print("No")
    else:
        cnt = 0
        for a in C:
            if C[a]%2==1:
                cnt += 1
        if cnt==1:
            print("Yes")
        else:
            print("No")
elif H%2==0 and W%2==0:
    flag = 0
    for a in C:
        if C[a]%4>0:
            flag = 1
            break
    if flag==0:
        print("Yes")
    else:
        print("No")
elif H%2==0:
    cnt = 0
    flag = 0
    for a in C:
        if C[a]%2==1:
            flag = 1
            break
        if C[a]%4==2:
            cnt += 1
    if flag==1:
        print("No")
    else:
        if cnt<=H//2:
            print("Yes")
        else:
            print("No")
elif W%2==0:
    cnt = 0
    flag = 0
    for a in C:
        if C[a]%2==1:
            flag = 1
            break
        if C[a]%4==2:
            cnt += 1
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
        if C[a]%2==1:
            cnt1 += 1
        if C[a]%4==2:
            cnt2 += 1
    if cnt1!=1:
        print("No")
    else:
        if cnt2<=(H+W-2)//2:
            print("Yes")
        else:
            print("No")