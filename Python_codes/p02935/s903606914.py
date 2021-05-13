n=int(input())
A=list(map(int,input().split()))
A=sorted(A,reverse=True)
s=0
for i in range(1,n):
    s+=A[i-1]/(2**i)
s+=A[n-1]/(2**(n-1))
print(s)