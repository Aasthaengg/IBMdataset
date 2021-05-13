while 1:
    r=0
    S=0
    n=int(input())
    if n==0:break
    s=list(map(int,input().split()))
    print(sum([((sum(s)/n)-i)**2/n for i in s])**0.5)