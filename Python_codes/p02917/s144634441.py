N = int(input())
B = [10**6]+list(map(int,input().split()))+[10**6]
A = [0]*N

for p in range(N):
    A[p] = min(B[p], B[p+1])

print(sum(A))


