n, k = map(int, input().split())
xlis = list(map(int, input().split()))
ret = 10 ** 100
for i in range(n-k+1):
    min_val = xlis[i]
    max_val = xlis[k+i-1]
    if min_val * max_val >= 0:
        tmp = max(abs(min_val), abs(max_val))
        ret = min(ret, tmp)
    else:
        fst = min(abs(min_val), abs(max_val))
        lst = max(abs(min_val), abs(max_val))
        tmp = fst * 2 + lst
        ret = min(ret, tmp)

print(ret)
