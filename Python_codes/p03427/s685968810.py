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
        n[0] -= 1
        for i in range(1,m):
            n[i] = 9
    print(sum(n))