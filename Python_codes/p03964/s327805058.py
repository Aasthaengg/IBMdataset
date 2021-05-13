N=int(input())
import copy
inp=[]
for i in range(N):
    inp.append(list(map(int,input().split(" "))))

def compare(A,B):
    if A[0]>=B[0] and A[1]>=B[1]:
        return A
    else:
        if B[0]%A[0]!=0:
            i=B[0]//A[0]+1
        else:
            i=B[0]//A[0]
        if B[1]%A[1]!=0:
            j=B[1]//A[1]+1 
        else:
            j=B[1]//A[1]
        m=max(i,j)
        return [A[0]*m,A[1]*m]
st=inp[0]
for i in range(1,N):
    st=compare(inp[i],st)
print(sum(st))