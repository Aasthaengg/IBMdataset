N = int(input())
A = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7
flag = True
if N % 2 == 0:
    for i in range(N // 2):
        if A[2 * i] != 2 * i + 1 or A[2 * i + 1] != 2 * i + 1:
            flag = False
else:
    if A[0] != 0:
        flag = False
    for i in range(1, N // 2 + 1):
        if A[2 * i - 1] != 2 * i or A[2 * i] != 2 * i:
            flag = False
if flag:
    print((2 ** (N // 2)) % mod)
else:
    print(0)
