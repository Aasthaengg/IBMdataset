N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_sum, b_sum = sum(A), sum(B)
turns = b_sum - a_sum
a_small = 0
b_small = 0
for a, b in zip(A,B):
    if a < b:
        a_small += (b - a + 1) // 2
    else:
        b_small += a - b
if a_small <= turns and b_small <= turns:
    print('Yes')
else:
    print('No')