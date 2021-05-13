A,B,K=map(int,input().split())
if A-K>0:
    print(A-K,B)
elif A-K<=0 and  A+B-K>=0:
    print(0,A+B-K)
elif A-K<=0 and A+B-K<0:
    print(0,0)

