N=int(input())
A=int(input())
ans=N%500
if ans-A<=0:
    print('Yes')
else:
    print('No')