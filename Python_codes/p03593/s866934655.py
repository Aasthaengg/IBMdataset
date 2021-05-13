from collections import Counter
H,W=map(int,input().split())
A=[]
for _ in range(H):
    A+=list(input())

#基本的に4個ずつないとダメ
#行数・列数が奇数の場合、真ん中の行・列は2個ずつでよい
#行数・列数が両方とも奇数の場合、全体の中心は1個でよい

C=Counter(A)
g4=0
g2=0
g1=0
for n in C.values():
    g4+=n//4
    g2+=(n%4)//2
    g1+=(n%4)%2

ans='No'
if (g1==1 and H&1 and W&1) or g1==0:
    if g4 >= (H//2)*(W//2):
        if (g2 + (g4 - (H//2)*(W//2))*2) == (H//2 if W&1 else 0) + (W//2 if H&1 else 0):
            ans='Yes'
print(ans)