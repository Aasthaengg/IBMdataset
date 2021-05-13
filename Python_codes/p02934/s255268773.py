n = int(input())
A = [int(x) for x in input().split()]

all_b = 0
for i in range(n):
    all_b += (1/A[i])

print(1/all_b)