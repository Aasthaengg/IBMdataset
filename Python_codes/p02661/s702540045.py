N=int(input())
A=[]
B=[]

for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

l=[]
r=[]
A.sort()
B.sort()

if N%2==1:
    n=N//2
    ans=B[n]-A[n]+1
else:
    n1=N//2-1
    n2=N//2
    ans=B[n1]-A[n1]+B[n2]-A[n2]+1

print(ans)