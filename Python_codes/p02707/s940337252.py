N = int(input())
A = list(map(int,input().split()))
buka = [0 for i in range(N)]
for i in range(2,N+1):
    joshi = A[i-2]
    buka[joshi-1] += 1

for i in buka:
    print(i)
