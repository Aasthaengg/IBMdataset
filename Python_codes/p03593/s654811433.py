H,W=map(int,input().split())
X=[0 for i in range(26)]
a=[list(input()) for i in range(H)]
for i in range(H):
    for j in range(W):
        X[ord(a[i][j])-97]+=1
A=[i%4 for i in X]
B=[i%2 for i in X]
if H%2==0 and W%2==0:
    if sum(A)==0:
        print("Yes")
    else:
        print("No")
elif H%2==1 and W%2==1:
    if sum(B)==1 and sum(A)<=H+W-1:
        print("Yes")
    else:
        print("No")
else:
    if H%2==0:
        H,W=W,H
    #H:odd
    if sum(B)==0 and sum(A)<=W:
        print("Yes")
    else:
        print("No")
