N = int(input())


def digit(i, j):
    """
    1 <= k <= N となる k で、先頭の桁が i , 末尾の桁が j となる物の数を返す
    """
    count = 0
    for k in range(1, N+1):
        if str(k)[0] == str(i) and k % 10 == j:
            count += 1
    return count


seen = {}
for i in range(1, 10):
    for j in range(1, 10):
        seen[(i, j)] = digit(i, j)

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        res += seen[(i, j)] * seen[(j, i)]


print(res)