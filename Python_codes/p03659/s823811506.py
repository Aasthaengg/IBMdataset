N=int(input())
*A,=map(int,input().split())
S=sum(A)

count=[[]for _ in range(N-1)]
count[0]=[A[0],S-A[0]]
i=1
while i<N-1:
    count[i]=[A[i]+count[i-1][0],S-(A[i]+count[i-1][0])]
    i+=1

print(min(abs(l-r) for l,r in count))