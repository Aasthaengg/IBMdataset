K,A,B=map(int,input().split())
if(A>=B-1 or K<A-1):
    print(K+1)
    exit()
res=K-A+1
if(res%2==0):
    print((B*(res//2))-(A*((res//2)-1)))
else:
    print((B*(res//2))-(A*((res//2)-1))+1)