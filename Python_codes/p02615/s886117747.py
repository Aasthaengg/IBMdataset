n=int(input())
A=list(map(int,input().split()))
A=sorted(A,reverse=True)
#print(A)
i=1
s=A[0]
while i<n-1:
    i+=1
    s+=A[i//2]
print(s)    