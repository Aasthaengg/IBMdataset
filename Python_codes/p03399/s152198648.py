A = [int(input()) for i in range(4)]
ans=0
if A[0]<A[1]:
    ans+=A[0]
else:
    ans= ans+A[1]
if A[2]<A[3]:
    ans+=A[2]
else:
    ans+=A[3]
print(ans)