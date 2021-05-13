N = int(input())
A = list(map(int,input().split()))
xor = A[0]

for i in range(1,N,1):
    xor = xor ^ A[i]

ans = map(str,[i^xor for i in A])

print(' '.join(ans))