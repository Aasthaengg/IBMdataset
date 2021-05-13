n = int(input())
A = list(map(int, input().split()))

i = 1
ans = 1
flg = 0
for i, j in zip(A[:-1],A[1:]):
    if i < j:
        if flg == 0:
            flg = 1
        elif flg == 2:
            ans += 1
            flg = 0
    if i > j:
        if flg == 0:
            flg = 2
        elif flg == 1:
            ans += 1
            flg = 0
print(ans)