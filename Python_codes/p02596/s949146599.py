K=int(input())
sevens=7
result=1
if K%2==0 or K%5==0:
    print(-1)
else:
    while sevens%K!=0:
        sevens%=K
        sevens=sevens*10+7
        result+=1
    print(result)