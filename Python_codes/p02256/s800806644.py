def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


alllist = list(map(int, input().split()))
alllist = sorted(alllist, reverse=True)


result = gcd(alllist[0], alllist[1])
print(result)

