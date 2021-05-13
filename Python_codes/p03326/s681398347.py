m, n = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(m)]


val = 0
temp_list = []

for i in range(2**3):
    temp_list = []
    op = [-1] * 3
    for j in range(3):
        if ((i >> j) & 1):
            op[3 - 1 - j] = 1

    for k in range(m):
        temp_list.append((op[0]*c[k][0])+(op[1]*c[k][1])+(op[2]*c[k][2]))
        temp_list.sort(reverse=True)
    val = max(val, sum(temp_list[:n]))
print(val)
