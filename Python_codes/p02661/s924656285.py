n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()
if n%2 == 0:
    x = A[n//2-1]+A[n//2]
    y = B[n//2-1]+B[n//2]
    ans = y-x+1
else:
    x = A[n//2]
    y = B[n//2]
    ans = y-x+1
print(ans)
