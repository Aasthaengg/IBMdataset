n, m = map(int,input().split())
a_mat = [input() for _ in range(n)]
b_mat = [input() for _ in range(m)]

contain = False
for i in range(n-m+1):
    for j in range(n-m+1):
        ok = True
        for k in range(m):
            if not ok:
                break
            for l in range(m):
                if a_mat[i+k][j+l] != b_mat[k][l]:
                    ok = False
                    break
        if ok:
            contain = True
            break
if contain:
    print("Yes")
else:
    print("No")
