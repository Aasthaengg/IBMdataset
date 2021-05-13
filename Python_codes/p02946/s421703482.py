k, x = map(int,input().split())

mi = min(1000000, x - k + 1)
ma = max(-1000000, x + k - 1)

for i in range(mi, ma+1):
    print(i)