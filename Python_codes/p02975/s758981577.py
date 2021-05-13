N=int(input())
A=list(map(int,input().split()))

A_set=set(A)
A_lst=list(A_set)

# すべてが0のとき
if sum(A_set)==0 and len(A_set)==1:
    print('Yes')
    exit()

# x…2N/3,0…N/3
if len(A_set)==2 and A_lst.count(0)==1 and len(A)%3==0:
    cnt=0
    for i in range(N):
        if A[i]==0:
            cnt+=1
    if cnt==N//3:
        print('Yes')
    else:
        print('No')
    exit()

# x^y^z==0
if len(A_set)==3 and A_lst[0]^A_lst[1]^A_lst[2]==0 and len(A)%3==0:
    cnt_x,cnt_y,cnt_z=0,0,0
    x,y,z=A_lst[0],A_lst[1],A_lst[2]
    for i in range(N):
        if A[i]==x:
            cnt_x+=1
            continue
        if A[i]==y:
            cnt_y+=1
            continue
        if A[i]==z:
            cnt_z+=1
    if cnt_x==cnt_y==cnt_z:
        print('Yes')
    else:
        print('No')
    exit()

# それ以外
print('No')