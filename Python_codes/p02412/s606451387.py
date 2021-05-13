def get_num(n, x):
    ans = 0
    for n3 in range(min(n, x), (x + 2) / 3, -1):
        for n2 in range(n3 - 1, (x - n3 + 1) / 2 - 1, -1):
            for n1 in range(n2 - 1, 0, -1):
                s = n1 + n2 + n3
                if s < x:
                    break
                elif s == x:
                    ans += 1
                    break
    return ans


while True:
    [n, x] = [int(m) for m in raw_input().split()]
    if [n, x] == [0, 0]:
        break
    if x == 0:
        print(0)
    else:
        print(get_num(n, x))