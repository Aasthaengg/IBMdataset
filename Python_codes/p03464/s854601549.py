K = int(input())
A = list(map(int,input().split()))
B = [2,2]
for i in range(K-1,-1,-1):
    a = A[i]
    bmin = B[0]
    bmax = B[1]
    if bmin%a==0:
        bmin = bmin
    else:
        bmin = (bmin//a+1)*a
    if bmin>bmax:
        B = []
        break
    else:
        if bmax%a==0:
            bmax = bmax+a-1
        else:
            bmax = (bmax//a)*a+a-1
        B = [bmin,bmax]
if len(B)==0:
    print(-1)
else:
    print(B[0],B[1])