#E
import sys
input=sys.stdin.readline

N=int(input())
A=[0 for i in range(N)]
B=[0 for i in range(N)]

for i in range(N):
    A[i],B[i]=map(int,input().split())
    
A_sort=sorted(A)
B_sort=sorted(B)

if N%2==0:
    f=(A_sort[int(N/2)]+A_sort[int(N/2)-1])/2
    t=(B_sort[int(N/2)]+B_sort[int(N/2)-1])/2
    ans=int((t-f)*2+1)
else:
    f=A_sort[int((N-1)/2)]
    t=B_sort[int((N-1)/2)]
    ans=int((t-f)+1)
    
print(ans)