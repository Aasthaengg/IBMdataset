n=int(input())
if n>10**6 or 1>n:
    pass
else:
    result=0
    for i in range(1,n+1,1):
        if i%3==0 and i%5==0:
            pass
        elif i%3==0:
            pass
        elif i%5==0:
            pass
        else:
            result+=i
        
    print(result)