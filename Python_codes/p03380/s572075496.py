n = int(input())
A = list(map(int,input().split()))
A.sort()
y = max(A)
x = A[0]
for a in A:
    if abs(y/2-a) < abs(y/2 - x):
        x = a
print(y, x)