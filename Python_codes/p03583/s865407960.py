#Tenka1_C
N = int(input())
def solve(h, n):
    x = N * h * n
    y = 4 * h * n - N * (n + h)
    if y <= 0:
        return -1
    if x % y == 0:
        return x // y
    else:
        return -1
    
flg = False
for h in range(1, 3501):
    if flg: break
    for n in range(1, 3501):
        if flg: break
        if solve(h, n) != -1:
            print(h, n, solve(h, n))
            flg = True