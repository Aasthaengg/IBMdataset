from collections import Counter


N = int(input())
A = list(map(int, input().split()))

C = Counter(A)

isAble = True
k = N - 1
while k >= 0:
    if k == 0:
        if C[k] != 1:
            isAble = False
    else:
        if C[k] != 2:
            isAble = False
    k -= 2

if isAble:
    print(pow(2, N // 2, 10 ** 9 + 7))
else:
    print(0)
