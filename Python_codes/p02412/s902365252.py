def get_num(n, m):
    ans = 0
    for x in range(n, 2, -1):
        if 3 * x - 2 < m:
            return ans
        for y in range(x - 1, 1, -1):
            if x + 2 * y - 1 < m:
                break
            for z in range(y - 1, 0, -1):
                s = x + y + z
                if s == m:
                    ans += 1
    return ans


while True:
    [n, m] = [int(x) for x in raw_input().split()]
    if [n, m] == [0, 0]:
        break
    print(get_num(n, m))