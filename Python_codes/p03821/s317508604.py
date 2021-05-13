n = int(input())
A,B = [],[]
for i in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    
A,B = A[::-1],B[::-1]

num = 0
for i in range(n):
    A[i] +=num
    if A[i]%B[i] !=0:
        num = num + B[i] - A[i]%B[i]
        #print(num,B[i], B[i] - A[i]%B[i])
print(num)