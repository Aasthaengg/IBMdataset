N,K=map(int,input().split())

result=0

if K%2==1:
    #全てKの倍数でないといけない
    result=(N//K)**3
else:
    #全てKの倍数
    result=(N//K)**3

    #またはすべて余りがk/2でなければならない
    if (N//K)*K+K/2<=N:
        result+=(N//K+1)**3
    else:
        result+=(N//K)**3

print(result)
