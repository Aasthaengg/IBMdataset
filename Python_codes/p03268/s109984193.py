n, k = list(map(int, input().split()))

print(((n//k)**3) + (((n-k//2)//k + 1)**3 if k%2 == 0 else 0))