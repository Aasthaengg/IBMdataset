N = int(input())
A = list(map(int,input().split()))
SUMA = sum(A)
SUMI = 0
MIN = float('inf')
for i in range(N-1):
    SUMI += A[i]
    MIN = min(MIN,abs(SUMA-2*SUMI))
print(MIN)