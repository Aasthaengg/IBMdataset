N=int(input())
*A,=map(int,input().split())
S=sum(A)

count1=0
count2=[0]*N
i=0
while i<N:
    count1+=A[i]
    count2[i]=abs(S-2*count1)
    i+=1

print(min(count2))