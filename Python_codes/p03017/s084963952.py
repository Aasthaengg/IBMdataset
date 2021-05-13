N,A,B,C,D = map(int,input().split())
S = list(input().strip())
S.insert(0,0)
if C<D:
    flag = 0
    for i in range(A+1,C+1):
        if S[i-1]=="#" and S[i]=="#":
            flag = 1
            break
    for i in range(B+1,D+1):
        if S[i-1]=="#" and S[i]=="#":
            flag = 1
            break
    if flag==0:
        print("Yes")
    else:
        print("No")
else:
    flag = 0
    for i in range(A+1,C+1):
        if S[i]=="#" and S[i-1]=="#":
            flag = 1
            break
    if flag == 0:
        flag1 = 1
        for i in range(B,D+1):
            if i+1<=N and S[i-1]=="." and S[i]=="." and S[i+1]==".":
                flag1 = 0
                break
        if flag1==1:
            flag = 1
    if flag==0:
        print("Yes")
    else:
        print("No")