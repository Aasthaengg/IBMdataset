n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
count = 0
for i in range(n - 1, -1, -1):
    count += (-(A[i] + count)) % B[i]
print(count)