def kai(n):
    a=1
    for i in range(1,n+1):
        a=a*i
    return a

N,M=map(int,input().split())
if N==0 or N==1:
    g=0
else:
    g=kai(N)/(kai(N-2)*2)
if M==0 or M==1:
    k=0
else:
    k=kai(M)/(kai(M-2)*2)
print(int(g+k))