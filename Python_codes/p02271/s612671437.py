n = int(input())
A = list(map(int, input().split()))
q = int(input())
nums = list(map(int, input().split()))

sum_set = set()
for i in range(1, 2 ** n):
    total = 0
    for j in range(n):
        if i >> j & 1:
            total += A[j]
    sum_set.add(total)

for num in nums:
    print('yes' if num in sum_set else 'no')

