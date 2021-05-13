N,A,B=map(int,input().split())
if (B-A)%2==0:
    print((B-A)//2)
else:
    tmp=A-1+(B-A+1)//2
    a=A+(N-B);b=N
    tmpp=N-B+(b-a+1)//2
    print(min(tmp,tmpp))