N, M, Q = map(int, input().split())

# i 以下に一切含まれていない数 つまり、l以下
# l_list = {}

# # i 以下に全て含まれている数 つまり、r以上
# r_list = {}
# L = []
# R = []
X = [[0]*N for _ in range(N)]

for i in range(M):
    l, r = map(int, input().split())
    X[l-1][r-1] += 1
    # L.append(l)
    # R.append(r)

C = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if j == 0:
            C[i][j] = X[i][j]
        else:
            C[i][j] = C[i][j-1] + X[i][j]

check = []
for i in range(Q):
    p, q = map(int, input().split())
    check.append((p,q)) 

for p,q in check:
    ans = 0
    for i in range(p-1,q):
        if p-2 < 0:
            ans += C[i][q-1]
        else:
            ans += C[i][q-1] - C[i][p-2]

    print(ans)