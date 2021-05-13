k, a, b = map(int, input().split())
if a >= (b-1):
    print(k+1)
else:
    res = a
    k -= (a - 1)
    res += (b-a) * (k//2)
    res += 1 if (k%2==1) else 0
    print(res)
