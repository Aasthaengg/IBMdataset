n = int(input())
A = []

B = list(map(int, input().split()))

sum_b = sum(B)
left = 0
for i in range(n-1):
    left += B[i]
    right = sum_b - left
    A.append(abs(right - left))
print(min(A))