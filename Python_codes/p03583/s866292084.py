N=int(input())

flag=False
def chk(h,n,w,N):
    val1=4*h*n*w
    val2=N*(n*w+h*w+h*n)
    if val1==val2:
        return True
    else:
        return False
def calc(h,n,N):
    if (4*h*n-(n+h)*N)==0:
        return -1
    val=(N*h*n)//(4*h*n-(n+h)*N)
    return val
for h in range(1,3501):
    for n in range(1,3501):
        w=calc(h,n,N)
        if w<=0:
            continue
        else:
            if chk(h,n,w,N):
                ans=[h,n,w]
                print(*ans)
                exit()
