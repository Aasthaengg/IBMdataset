N=int(input())
l=list(map(int,input().split()))

if sum(l)-2*max(l)>0:
    print("Yes")
else:
    print("No")