n=int(input())
L=list(map(int,input().split()))
L_max=max(L)
L_sum=sum(L)
if 0<L_sum-L_max*2:
    print("Yes")
else:
    print("No")