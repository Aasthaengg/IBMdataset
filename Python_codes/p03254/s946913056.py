n,x=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)
if x>sum(A):
    print(len(A)-1)
if x==sum(A):
    print(len(A))
if x<sum(A):
    ans=0
    for i in range(len(A)):
        if x>=A[i]:
            x-=A[i]
            ans+=1
        else:
            print(ans)
            break