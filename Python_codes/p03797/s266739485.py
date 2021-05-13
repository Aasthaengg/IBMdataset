N,M=map(int,input().split())
ans = 0
if M%2==0:
    x=M//2
    if N>=x:
        print(x)
        exit()
    else:
        ans+=N
        y=M-N*2
        z=y//4
        ans+=z
else:
    x=M//2
    if N>=x:
        print(x)
        exit()
    else:
        ans+=N
        y=M-N*2
        z=y//4
        ans+=z
print(ans)