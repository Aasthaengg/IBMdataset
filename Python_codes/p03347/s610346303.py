N=int(input())
A=[int(input()) for i in range(N)]
def Solve(n,A):
    if n==1:
        return -1 if A[0]!=0 else 0
    else:
        ret=0
        for i in range(n):
            if i==0:
                if A[i]!=0:
                    return -1
            else:
                if A[i]==A[i-1]+1:
                    ret+=1
                elif A[i]<=A[i-1]:
                    ret+=A[i]
                else:
                    return -1
        return ret
print(Solve(N,A))