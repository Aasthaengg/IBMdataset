n = int(input())
A = list(map(int, input().split()))

even = []
odd = []

for i in range(0, n, 2):
    even.append(A[i])
for i in range(1, n, 2):
    odd.append(A[i])

if (n-1) % 2 == 0:
    even.reverse()
    ans = even + odd
else:
    odd.reverse()
    ans = odd + even

print(*ans)
