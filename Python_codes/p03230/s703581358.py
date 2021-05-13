def is_square(N):
    i = 0
    while i**2 < N:
        i += 1
    if i**2 == N:
        return i
    return None


N = int(input())
r = is_square(8*N+1)
if r is None:
    print("No")
else:
    print("Yes")
    k = (r-1)//2
    size = k+1
    print(size)
    length = k
    ans = [[-1]*length for _ in range(size)]
    used = set()
    cur_max = 0
    for i in range(0, size):
        for j in range(i):
            ans[i][j] = ans[j][i-1]
        for k in range(i, length):
            ans[i][k] = cur_max+1
            cur_max += 1
    for a in ans:
        print("{} {}".format(length, " ".join(map(str, a))))
