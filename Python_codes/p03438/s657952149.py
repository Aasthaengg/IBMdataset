import math

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_a = sum(a)
sum_b = sum(b)
num_b = 0
num_a = 0
for i in range(n):
    if a[i] > b[i]:
        num_b += a[i] - b[i]
    else:
        num_a += math.ceil((b[i]-a[i])/2)

if sum_b-sum_a >= num_b and sum_b-sum_a >= num_a:
    print('Yes')
else:
    print('No')