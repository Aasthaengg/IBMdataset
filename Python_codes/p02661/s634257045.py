n = int(input())

A = []
B = []

for i in range(n):
   a, b = map(int, input().split())
   A.append(a)
   B.append(b)

A.sort()
B.sort()

ans = 0

if n % 2 == 1:
    l1 = A[int(n/2)]
    r1 = B[int(n/2)]
    ans = r1 - l1 + 1
else:
    l2 = A[int(n/2)-1] + A[int((n/2))]
    r2 = B[int(n/2)-1] + B[int((n/2))]
    ans = r2 - l2 + 1

print(ans)


