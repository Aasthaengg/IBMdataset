N=int(input())
length=list(map(int,input().split()))
long=max(length)

total=sum(length)
semi_total=total-long
if semi_total>long:
    print('Yes')
else:
    print('No')