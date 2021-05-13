import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
# print(A)
# print(B)

# a <= b のところは一致させることができる
# a > b となっているところを a = b にするのに必要な+1の操作数を、
# a <= b となっているところが a <= b のままである「余裕な走査数」が上回っていれば良い
need_an = 0
need_bn = 0
for i in range(N):
    if A[i] > B[i]:
        need_bn += A[i] - B[i]
    elif A[i] < B[i]:
        need_an += (B[i] - A[i]) // 2

# print(need_an, need_bn)
if need_an >= need_bn:
    print("Yes")
else:
    print("No")