n = int(input())
A = []
X = []

for _ in range(n):
    a = int(input())
    A.append(a)
    Y = []
    for _ in range(a):
        x, y = map(int, input().split())
        Y.append(x)
        Y.append(y)
    X.append(Y)

# print("X",X)
ans = 0

for i in range(2**n):
    flg = True
    honest = [0]*n
    count = 0
    for j in range(n):
        if ((i >> j) & 1):
            honest[j] = 1
    # print("honest",honest)
    for k in range(n):
        for l in range(0,len(X[k]),2):
            # print(honest[X[k][l]-1], X[k][l+1])
            if honest[X[k][l]-1] != X[k][l+1] and honest[k] == 1:
                # print('hi')
                flg = False

    if flg:
        count = sum(honest)
        # print("count", count)
        ans = max(ans, count)



print(ans)