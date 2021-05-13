import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
# print(A)
# print(B)

sum_a = sum(A)
sum_b = sum(B)
need_n = sum_b - sum_a

need_an = 0
need_bn = 0
for i in range(N):
    if A[i] > B[i]:
        need_bn += A[i] - B[i]
    elif A[i] < B[i]:
        tmp = B[i] - A[i]
        need_an += tmp // 2

# print(need_n, need_an, need_bn)
if sum_a <= sum_b and need_an >= need_bn:
    print("Yes")
else:
    print("No")