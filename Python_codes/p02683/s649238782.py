def main():
    n, m, x = map(int, input().split())
    sofar = 10 ** 5 + 1
    cl = list(list(map(int, input().split())) for _ in range(n))
    # print(cl)
    ans = float('inf')
    for i in range(2 ** n):
        tmp = [0] * m
        cost = 0
        for j in range(n):
            # print(bin(j), i, bin(i >> j))
            if (i >> j) & 1:
                for k in range(m):
                    tmp[k] += cl[j][k + 1]
                cost += cl[j][0]
                # print(tmp)
        for t in tmp:
            if t < x:
                break
        else:
            ans = min(ans, cost)
    if ans == float('inf'):
        return -1
    else:
        return ans


if __name__ == '__main__':
    print(main())
