import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

B = [-1 for _ in range(N)]
ans = []

for i in range(N, 0, -1):
    tmp_sum = 0
    tmp_i = 2 * i
    while N >= tmp_i:
        tmp_sum += B[tmp_i - 1]
        tmp_i += i

    if A[i-1] == tmp_sum % 2:
        B[i-1] = 0
    else:
        ans.append(i)
        B[i-1] = 1

print(len(ans))
if len(ans):
    print(" ".join(map(str, ans[::-1])))
