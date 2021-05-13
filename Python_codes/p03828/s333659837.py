def solve(n):
    l = [1 for i in range(n+1)]
    for k in range(2,n+1):
        tmp = k
        i = 2
        while tmp > 1:
            if tmp % i == 0:
                tmp = tmp // i
                l[i] += 1
            else:
                i += 1
    res = 1
    for i in l:
        res = res * i % (10**9+7)
    return res

if __name__ == '__main__':
    n = int(input())
    print(solve(n))