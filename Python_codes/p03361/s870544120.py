H,W = map(int,input().split())
S = ["."*(W+2)]
for _ in range(H):
    a = input().strip()
    a = "."+a+"."
    S.append(a)
S.append("."*(W+2))
flag = 0
for i in range(1,H+1):
    for j in range(1,W+1):
        if S[i][j]=="#":
            if S[i][j+1]=="." and S[i-1][j]=="." and S[i][j-1]=="." and S[i+1][j]==".":
                flag = 1
                break
    if flag==1:break
if flag==0:
    print("Yes")
else:
    print("No")