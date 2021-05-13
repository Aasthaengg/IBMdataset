A,B,K=map(int,input().split())
ans=0
n=100
while True:
    if A%n==0 and B%n==0:
        ans+=1
        if ans==K:
            print(n)
            exit()
    n-=1
