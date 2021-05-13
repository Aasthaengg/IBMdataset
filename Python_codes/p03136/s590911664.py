N=int(input())
L=list(map(int,input().split()))

a=max(L)
sum=sum(L)

if a<sum-a:
    print("Yes")
else:
    print("No")