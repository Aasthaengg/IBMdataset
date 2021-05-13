def calc(n):
    if res[n] != 0:
        return res[n]
    tmp = calc(n-1) + calc(n-2)
    res[n] = tmp
    return tmp

N = int(input())
res = [0] * 100
res[0] = 2
res[1] = 1
calc(N)
print(res[N])