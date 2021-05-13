X, N = map(int, input().split(' '))
if N == 0:
    print(X)
else:
    P_ls = list(map(int, input().split(' ')))
    diff, rst = -1, 0
    for i in range(101, -1, -1):
        if i not in P_ls:
            if diff == -1:
                diff = abs(X - i)
                rst = i
            else:
                diff = min(diff, abs(X - i))
                if diff == abs(X - i):
                    rst = i
    print(rst)