import sys

K, T = map(int, input().split())
A = list(map(lambda x, y: [int(x), y], sys.stdin.readline().rsplit(), range(T)))
A.sort(reverse=True)

if T == 1:
    print(K - 1)
    exit()

res = 0
pre = -1
t = []
for k in range(K):
    if pre != A[0][1]:
        A[0][0] -= 1
        pre = A[0][1]
    elif pre == A[0][1] and A[1][0] > 0:
        A[1][0] -= 1
        pre = A[1][1]
    else:
        res += 1
    A.sort(reverse=True)

print(res)
