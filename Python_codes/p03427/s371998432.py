n = list(input())
n = [int(i) for i in (n)]
m = len(n)
if m == 1:
    print(n[0])
else:
    flg = False
    for i in range(1,m):
        if n[i] != 9:
            flg = True
            break
    if flg:
        print(n[0] - 1 + 9 * (m - 1))
    else:
        print(sum(n))