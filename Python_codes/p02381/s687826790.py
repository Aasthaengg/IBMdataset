while True:
    n=int(input())
    if n==0:
        break
    S=[]
    S=list(map(int,input().split()))
    m=sum(S)/n
    a=0
    for i in range(n):
       a+=(S[i]-m)**2
    a/=n
    print(a**0.5)