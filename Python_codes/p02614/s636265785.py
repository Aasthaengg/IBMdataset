from sys import stdin,stdout
def fn(mask_r,mask_c):
    cells=0
    for cur_r in range(r):
        for cur_c in range(c):
            if mask_c &(1<<cur_c)==0 or mask_r&(1<<cur_r)==0:continue
            if a[cur_r][cur_c]=='#':cells+=1
    return cells==k
for _ in range(1):#int(stdin.readline())):
    # n=int(stdin.readline())
    ans=0
    r,c,k= map(int,stdin.readline().split())
    a=[input() for _ in range(r)]
    for mask_r in range(1<<r):
        for mask_c in range(1<<c):
            # print(bin(mask_r)[2:],bin(mask_c)[2:])
            if fn(mask_r,mask_c):ans+=1
    print(ans)
