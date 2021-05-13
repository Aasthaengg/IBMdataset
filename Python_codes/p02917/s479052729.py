n=int(input())
B = list(map(int,input().split()))
A= B[0]
for i in range(1,n-1):
    A += min(B[i-1],B[i])
A+= B[n-2]
print(A)