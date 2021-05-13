N = int(input())
A = list(map(int, input().split()))

now = sum(A)
for i in range(N//2):
    now -= 2*A[2*i+1]

for a in A:
    print(now, end=' ')
    X = 2*a - now
    now = X
print()
