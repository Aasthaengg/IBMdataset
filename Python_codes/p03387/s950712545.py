A=list(map(int,input().split()))
A.sort(reverse=True)
cnt=0
cnt+=A[0]-A[1]
if (A[0]-(A[2]+cnt))%2==0:
    print(cnt+(A[0]-(A[2]+cnt))//2)
else:
    print(cnt+(A[0]-(A[2]+cnt))//2+2)