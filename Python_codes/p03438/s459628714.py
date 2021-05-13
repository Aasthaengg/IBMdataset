n=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

k=sum(B)-sum(A)

ka=0
kb=0
for i in range(n):
    if A[i]>B[i]:
        kb+=A[i]-B[i]
    elif A[i]<B[i]:
        ka+=(B[i]-A[i]+1)//2
        kb+=(B[i]-A[i])%2

if k>=ka and k>=kb:
    print("Yes")
else:
    print("No")