N = int(input())
A = list(map(int,input().split()))
B = [0]*N
for i in range(N):
    while A[i]%2==0:
        B[i] +=1
        A[i] = A[i]//2
print(sum(B))
