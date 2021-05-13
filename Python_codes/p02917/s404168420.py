n =int(input())
B = list(map(int,input().split()))

A=[0]*n
i=0
A[i]=B[i]
while 1 :
    i+=1
    if i>=n-1:
        break
    A[i]=min(B[i],B[i-1])
A[i]=B[i-1]

# print(B)
# print(A)
print( sum(A) )