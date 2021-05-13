d, k = list(map(int, input().split()))
if k == 100:
    print(101 * (100**d))
else:
    print(k * (100**d))
