n, p = map(int ,input().split())
a = list(map(int ,input().split()))
flg_lst = []
for i in range(n):
    if a[i] % 2 == 0:
        flg_lst.append(True)
    else:
        flg_lst.append(False)
if False in flg_lst:
    print(2 ** (n - 1))
else:
    if p == 0:
        print(2 ** n)
    else:
        print(0)
