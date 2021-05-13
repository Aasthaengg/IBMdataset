N,M=map(int,input().split())
count=0
if N>=1 and M>=2:
    a=M//2
    if N>=a:
        M=M-2*a
        answer=a
    else:
        M=M-2*N
        answer=N
else:
    answer=0
if M>=4:
    kotae=M//4
else:
    kotae=0
print(answer+kotae)
