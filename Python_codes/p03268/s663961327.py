n,k = map(int,input().split())

if k % 2 == 1:
    knum = n // k
    print(knum ** 3)
else:
    knum = n // k
    kodd = (n + k // 2) // k
    print(knum ** 3 + kodd ** 3)