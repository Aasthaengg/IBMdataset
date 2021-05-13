N = int(input())
A = sorted([list(map(int,input().split())) for _ in range(N)],key=lambda x:x[2],reverse=True)
for x in range(101):
    for y in range(101):
        a,b,h = A[0]
        H = h+abs(x-a)+abs(y-b)
        flag = 1
        for i in range(1,N):
            a,b,h = A[i]
            if max(0,H-abs(x-a)-abs(y-b))==h:continue
            else:
                flag = 0
                break
        if flag==1:
            cx = x
            cy = y
            break
    if flag==1:break
print(cx,cy,H)