N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#print(A,B)
add = 0
for i in range(len(B)):
    if B[i] > A[i]:
        add += A[i]
        B[i] -=  A[i]
        if A[i+1] > B[i]:
            add+=B[i]
            A[i+1] -= B[i]
        else:
            add += A[i+1]
            A[i+1] = 0
    else:
        add+=B[i]
        B[i] = 0
    #print(A,B,add)
    
#add += min(A[-1],B[-1])
print(add)