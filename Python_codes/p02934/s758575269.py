N = int(input())
A = list(map(int,input().split()))
m = [1] * N
for i in range(0,len(A)):
    for j in range(0,len(A)):
        if i == j:
            continue
        else:
            m[i] *= A[j] 
print(m[0]*A[0]/sum(m))