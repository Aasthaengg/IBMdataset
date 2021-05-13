n = int(input())
A = [list(map(int,input().split())) for i in range(n)]

# B = [[[0, 0] for i in range(n)] for j in range(n)]
if n == 1:
    print(1)
else:

    D = {}
    for i in range(n):
        for j in range(n):
            if i != j:
                dy = A[i][1] - A[j][1]
                dx = A[i][0] - A[j][0]
                try:
                    D[(dx, dy)] += 1
                except:
                    D[(dx, dy)] = 1
    # print(D)
    ans = n - max(list(D.values()))
    print(ans)