n = int(input())
data = list(map(int, input().split()))
datb = list(map(int, input().split()))
datc = [data[i] - datb[i] for i in range(n)]
datc.sort(reverse=True)
#print(datc)
if sum(datc) < 0:
    print(-1)
else:
    l, r = 0, n-1
    res = 0
    total = 0
    import collections
    dat = collections.deque(datc)
    while len(dat) > 0:
        if total >= 0:
            v = dat.pop()
            if v >= 0:
                break
            res += 1
            total += v
        else:
            total += dat.popleft()
            res += 1
    print(res)
