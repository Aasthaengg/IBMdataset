n = int(input())
A = list(map(int,input().split()))
pre_col = A[0]
flg = False
res = 0
for i in range(1, n):
    if flg or A[i] != pre_col:
        pre_col = A[i]
        flg = False
    elif A[i] == pre_col:
        res += 1
        flg = True
print(res)