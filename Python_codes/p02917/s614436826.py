N = int(input())
A = [0]*N
B = list(map(int,input().split()))
B.append(10**5)
A[0] = B[0]
for n in range(1,N):
    A[n] = min(B[n-1],B[n])
print(sum(A))